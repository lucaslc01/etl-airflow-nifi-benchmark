from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from scripts.ingest_csv import load_csv_to_postgres


# =======================================================
# Caminhos e parâmetros específicos da DAG CNES
# =======================================================
CSV_PATH = "/mnt/c/Users/lucas/documents/TCC/tcc3/tabelas_padronizadas/cnes/CNES_padronizado.csv"
TABLE_NAME = "cnes_df"


# =======================================================
# Definição da DAG
# =======================================================
with DAG(
    dag_id="import_cnes_df",
    description="Importa o arquivo CNES.csv para a tabela cnes_df no PostgreSQL",
    start_date=datetime(2025, 10, 10),
    schedule_interval=None,  # execução manual
    catchup=False,
    tags=["SUS", "CNES", "ingestao"],
) as dag:

    ingest_cnes = PythonOperator(
        task_id="ingest_cnes",
        python_callable=load_csv_to_postgres,
        op_kwargs={
            "csv_path": CSV_PATH,
            "table_name": TABLE_NAME
        },
    )

    ingest_cnes
