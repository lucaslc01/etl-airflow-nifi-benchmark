from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from scripts.ingest_csv import load_csv_to_postgres

with DAG(
    dag_id="import_sia_df",
    schedule_interval=None,
    start_date=datetime(2025, 10, 10),
    catchup=False,
    tags=["SUS", "sia"]
) as dag:

    ingest_task = PythonOperator(
        task_id="ingest_sia_df",
        python_callable=load_csv_to_postgres,
        op_kwargs={
            "csv_path": "/mnt/c/Users/lucas/documents/TCC/tcc3/tabelas_padronizadas/sia/SIA_padronizado.csv",  # caminho final do CSV padronizado
            "table_name": "sia_df"  # nome da tabela destino no PostgreSQL
        }
    )
