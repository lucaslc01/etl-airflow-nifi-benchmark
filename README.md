# etl-airflow-nifi-benchmark
Performance benchmark of Apache Airflow and Apache NiFi for ETL pipelines using DATASUS healthcare data.

# ETL Benchmark: Apache Airflow vs Apache NiFi

Comparative benchmark of Apache Airflow and Apache NiFi for large-scale ETL pipelines using public Brazilian healthcare datasets from DATASUS.

## Architecture

```mermaid
flowchart TD
    A[DATASUS Public Datasets] --> B1[Apache Airflow Pipeline]
    A --> B2[Apache NiFi Pipeline]

    B1 --> C1[Data Extraction]
    C1 --> D1[Data Transformation]
    D1 --> E1[Data Loading]

    B2 --> C2[Data Ingestion]
    C2 --> D2[Flow Processing]
    D2 --> E2[Data Loading]

    E1 --> F[(PostgreSQL / Data Warehouse)]
    E2 --> F

    F --> G[Analytical SQL Queries]
    G --> H[Performance Evaluation]

    H --> I[Execution Time]
    H --> J[CPU Usage]
    H --> K[Memory Usage]
```

Dataset

The project used public Brazilian healthcare datasets, including:

SIA/DATASUS
CNES
SIGTAP
CID
CBO
Brazilian municipalities data

More than 40 million records were processed during the experiments.

etl-airflow-nifi-benchmark/
│
├── airflow/
│   └── dags/
│
├── nifi/
│   └── templates/
│
├── sql/
│
├── scripts/
│
├── diagrams/
│
├── images/
│
├── docs/
│
└── sample_data/

Important Note

The original experiments were executed using institutional infrastructure from CEFET-MG and CIT/UFMG, including Hadoop cluster resources.

For this reason, the complete execution environment cannot be fully reproduced using only this repository.

This repository focuses on documenting the architecture, source code, methodology and results obtained during the research.

Author

Lucas Loscheider Reis Muniz
Computer Engineering — CEFET-MG

LinkedIn: https://www.linkedin.com/in/lucas-loscheider


Depois clique em **Commit changes**.

Próximo passo: vamos criar a seção de **resultados**, com tabela comparando Airflow e NiFi.
