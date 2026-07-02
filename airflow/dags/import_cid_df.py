from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from scripts.ingest_csv import load_csv_to_postgres

with DAG(
    dag_id="import_cid_df",
    schedule_interval=None,
    start_date=datetime(2025, 10, 10),
    catchup=False,
    tags=["SUS", "cid"]
) as dag:

    ingest_task = PythonOperator(
        task_id="ingest_cid_df",
        python_callable=load_csv_to_postgres,
        op_kwargs={
            "csv_path": "/mnt/c/Users/lucas/documents/TCC/tcc3/tabelas_padronizadas/cid/CID_padronizado.csv",  # ajuste o caminho se necessário
            "table_name": "cid_df"
        }
    )
