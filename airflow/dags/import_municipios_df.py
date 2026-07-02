from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from scripts.ingest_csv import load_csv_to_postgres

with DAG(
    dag_id="import_municipios_df",
    schedule_interval=None,
    start_date=datetime(2025, 10, 10),
    catchup=False,
    tags=["SUS", "municipios"]
) as dag:

    ingest_task = PythonOperator(
        task_id="ingest_municipios",
        python_callable=load_csv_to_postgres,
        op_kwargs={
            "csv_path": "/mnt/c/Users/lucas/documents/TCC/tcc3/tabelas_padronizadas/municipios/municipios_standardized.csv",  # AJUSTE O LOCAL REAL
            "table_name": "municipios_df"               # AJUSTE AS COLUNAS/ESQUEMA
        }
    )
