from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from scripts.ingest_csv import load_csv_to_postgres

with DAG(
    dag_id="import_cbocod_df",
    schedule_interval=None,
    start_date=datetime(2025, 10, 10),
    catchup=False,
    tags=["SUS", "cbocod"]
) as dag:

    ingest_task = PythonOperator(
        task_id="ingest_cbocod_df",
        python_callable=load_csv_to_postgres,
        op_kwargs={
            "csv_path": "/mnt/c/Users/lucas/documents/TCC/tcc3/tabelas_padronizadas/cbocod/CBO_padronizado.csv",  # caminho real
            "table_name": "cbocod_df"
        }
    )
