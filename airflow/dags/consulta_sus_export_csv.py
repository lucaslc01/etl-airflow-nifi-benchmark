from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from datetime import datetime
import pandas as pd
import os


# ===============================================================
# Função que executa a consulta e salva em CSV
# ===============================================================
def executar_consulta_exportar_csv():

    # Conecta ao Postgres usando a conexão configurada no Airflow
    hook = PostgresHook(postgres_conn_id="postgres_sus")
    conn = hook.get_conn()
    cur = conn.cursor()

    # Caminho final do CSV
    output_dir = "/home/lucas/airflow/outputs"
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, "resultado_consulta_airflow.csv")

    # Consulta SQL completa
    sql = """
    SELECT 
        municipios_df.regiao,
        ano_mes_df.mes,
        cid_df.subcat,
        cid_df.descricao,
        SUM(sia_df.pa_qtdapr) AS procedimentos,
        SUM(sia_df.pa_valapr) AS valor
    FROM sia_df
    JOIN municipios_df 
        ON sia_df.pa_ufmun::INTEGER = (municipios_df.id_municipio / 10)
    JOIN ano_mes_df
        ON RIGHT(sia_df.pa_cmp, 2) = ano_mes_df.mes
    JOIN cnes_df
        ON sia_df.pa_coduni::VARCHAR = cnes_df.co_cnes
    JOIN sigtap_proced_df
        ON sia_df.pa_proc_id = sigtap_proced_df.codigo
    JOIN cid_df
        ON sia_df.pa_cidpri = cid_df.subcat
    JOIN sexo_df
        ON sia_df.pa_sexo = sexo_df.pa_sexo
    JOIN raca_cor_df 
        ON LPAD(sia_df.pa_racacor, 2, '0') = raca_cor_df.pa_racacor
    WHERE  cnes_df.no_razao_social ILIKE '%UNIDADE BASICA%'
      AND ano_mes_df.mes IN ('01', '02', '03', '04')
      AND sexo_df.sexo_desc = 'Masculino'
      AND raca_cor_df.racacor_desc = 'PRETA' 
    GROUP BY 
        municipios_df.regiao,
        ano_mes_df.mes,
        cid_df.subcat,
        cid_df.descricao
    ORDER BY 
        municipios_df.regiao ASC,
        ano_mes_df.mes ASC,
        SUM(sia_df.pa_valapr) DESC;
    """

    print("🚀 Executando consulta SQL...")
    cur.execute(sql)

    # Recupera o resultado
    rows = cur.fetchall()
    colnames = [desc[0] for desc in cur.description]

    # Cria DataFrame
    df = pd.DataFrame(rows, columns=colnames)

    # Salva o CSV
    df.to_csv(output_file, index=False, encoding="utf-8")

    print(f"✅ CSV gerado com sucesso: {output_file}")

    cur.close()
    conn.close()



# ===============================================================
# DAG do Airflow
# ===============================================================
with DAG(
    dag_id="consulta_sus_export_csv",
    description="Executa consulta SUS e exporta resultado para CSV",
    start_date=datetime(2025, 1, 1),
    schedule_interval=None,  # rodar manualmente
    catchup=False,
    tags=["SUS", "consulta", "export"]
) as dag:

    executar_consulta = PythonOperator(
        task_id="executar_consulta_exportar_csv",
        python_callable=executar_consulta_exportar_csv
    )
