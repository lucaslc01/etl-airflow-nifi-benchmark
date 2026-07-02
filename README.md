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
