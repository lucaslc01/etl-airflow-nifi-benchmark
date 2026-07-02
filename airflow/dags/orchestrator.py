from airflow import DAG
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from datetime import datetime
import os


# ========================================
# Função de validação
# ========================================
def validate_table(table_name):
    hook = PostgresHook(postgres_conn_id="postgres_sus")
    conn = hook.get_conn()
    cur = conn.cursor()
    cur.execute(f"SELECT COUNT(*) FROM {table_name};")
    linhas = cur.fetchone()[0]
    print(f"✔ {table_name}: {linhas:,} linhas")
    conn.close()


# ========================================
# Sinais para monitoramento externo
# ========================================
START_SIGNAL = "/home/lucas/airflow/monit_start"
STOP_SIGNAL = "/home/lucas/airflow/monit_stop"


def create_start_signal():
    if os.path.exists(START_SIGNAL):
        os.remove(START_SIGNAL)
    if os.path.exists(STOP_SIGNAL):
        os.remove(STOP_SIGNAL)
    with open(START_SIGNAL, "w") as f:
        f.write("start")
    print("🚀 Sinal de início criado.")


def create_stop_signal():
    with open(STOP_SIGNAL, "w") as f:
        f.write("stop")
    print("🏁 Sinal de fim criado.")


# ========================================
# DAG PRINCIPAL
# ========================================
with DAG(
    dag_id="sus_orchestrator",
    description="Orquestra ingestão + consulta + monitoramento externo",
    start_date=datetime(2025, 1, 1),
    schedule_interval=None,
    catchup=False,
) as dag:

    # Sinal de início do monitor
    task_start_monitor = PythonOperator(
        task_id="start_monitor",
        python_callable=create_start_signal
    )

    # DAGs individuais
    trigger_municipios = TriggerDagRunOperator(task_id="trigger_import_municipios_df", trigger_dag_id="import_municipios_df")
    validate_municipios = PythonOperator(task_id="validate_municipios_df", python_callable=lambda: validate_table("municipios_df"))

    trigger_cbocod = TriggerDagRunOperator(task_id="trigger_import_cbocod_df", trigger_dag_id="import_cbocod_df")
    validate_cbocod = PythonOperator(task_id="validate_cbocod_df", python_callable=lambda: validate_table("cbocod_df"))

    trigger_cid = TriggerDagRunOperator(task_id="trigger_import_cid_df", trigger_dag_id="import_cid_df")
    validate_cid = PythonOperator(task_id="validate_cid_df", python_callable=lambda: validate_table("cid_df"))

    trigger_sigtap = TriggerDagRunOperator(task_id="trigger_import_sigtap_proced_df", trigger_dag_id="import_sigtap_proced_df")
    validate_sigtap = PythonOperator(task_id="validate_sigtap_proced_df", python_callable=lambda: validate_table("sigtap_proced_df"))

    trigger_cnes = TriggerDagRunOperator(task_id="trigger_import_cnes_df", trigger_dag_id="import_cnes_df")
    validate_cnes = PythonOperator(task_id="validate_cnes_df", python_callable=lambda: validate_table("cnes_df"))

    trigger_sia = TriggerDagRunOperator(task_id="trigger_import_sia_df", trigger_dag_id="import_sia_df")
    validate_sia = PythonOperator(task_id="validate_sia_df", python_callable=lambda: validate_table("sia_df"))

    trigger_consulta = TriggerDagRunOperator(task_id="trigger_consulta", trigger_dag_id="consulta_sus_export_csv")

    # Sinal de finalização do monitor
    task_stop_monitor = PythonOperator(
        task_id="stop_monitor",
        python_callable=create_stop_signal
    )

    # Pipeline completo
    (
        task_start_monitor >>
        trigger_municipios >> validate_municipios >>
        trigger_cbocod >> validate_cbocod >>
        trigger_cid >> validate_cid >>
        trigger_sigtap >> validate_sigtap >>
        trigger_cnes >> validate_cnes >>
        trigger_sia >> validate_sia >>
        trigger_consulta >>
        task_stop_monitor
    )
