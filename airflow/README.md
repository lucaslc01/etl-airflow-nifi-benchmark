# Apache Airflow DAGs

This directory contains the Apache Airflow Directed Acyclic Graphs (DAGs) developed for the ETL benchmark.

Each DAG is responsible for importing or processing a specific healthcare dataset before executing the final analytical query.

## DAGs

| DAG | Description |
|------|-------------|
| import_municipios_df | Imports Brazilian municipalities dataset into PostgreSQL. |
| import_cbocod_df | Imports Brazilian Occupation Classification (CBO) dataset. |
| import_cid_df | Imports ICD (International Classification of Diseases) dataset. |
| import_sigtap_proced_df | Imports SIGTAP procedures dataset. |
| import_cnes_df | Imports CNES healthcare facilities dataset. |
| import_sia_df | Imports DATASUS outpatient production data. |
| consulta_sus_export | Executes the analytical SQL query and exports the benchmark results. |
| sus_orchestrator | Orchestrates the complete ETL workflow. |

## Technologies

- Apache Airflow
- Python
- PostgreSQL
- Docker

## Purpose

These DAGs were used during the benchmark to evaluate Apache Airflow performance regarding ETL execution, workflow orchestration and maintainability.
