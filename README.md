# ETL Benchmark: Apache Airflow vs Apache NiFi

> Comparative benchmark of Apache Airflow and Apache NiFi for large-scale ETL pipelines using Brazilian public healthcare datasets (DATASUS).

---

## Overview

This repository contains the source code, SQL scripts, Apache Airflow DAGs, Apache NiFi flows, documentation and benchmark results developed as the undergraduate thesis for the Computer Engineering degree at CEFET-MG.

The objective of this project was to compare Apache Airflow and Apache NiFi in equivalent ETL pipelines using real healthcare data, evaluating their performance, resource consumption and maintainability.

---

## Objectives

- Build equivalent ETL pipelines using Apache Airflow and Apache NiFi.
- Process large-scale healthcare datasets from DATASUS.
- Compare execution time, CPU usage and memory consumption.
- Evaluate workflow maintainability and scalability.
- Document the architecture and benchmark methodology.

---

## Technologies

| Category | Technologies |
|-----------|-------------|
| Programming | Python, SQL |
| ETL | Apache Airflow, Apache NiFi |
| Big Data | Apache Spark, Hadoop Hive |
| Database | PostgreSQL |
| Infrastructure | Docker, Linux |
| Version Control | Git, Bitbucket |

---

## Dataset

Public datasets used during the experiments:

- DATASUS (SIA)
- CNES
- SIGTAP
- CID
- Brazilian Municipalities

More than **42 million healthcare records** were processed during the benchmark.

---

## Repository Structure

```
etl-airflow-nifi-benchmark
│
├── airflow/
│   └── Apache Airflow DAGs
│
├── nifi/
│   └── Apache NiFi templates
│
├── sql/
│   └── SQL scripts
│
├── diagrams/
│   └── Database and ETL architecture diagrams
│
├── images/
│   └── Benchmark graphs and screenshots
│
├── docs/
│   └── Thesis documentation
│
├── README.md
├── LICENSE
└── .gitignore
```

---

## Benchmark Results

| Metric | Apache Airflow | Apache NiFi |
|---------|---------------:|------------:|
| Average execution time | 01:41:14 | 00:39:00 |
| Average CPU usage | ~3–4% | ~4–5% |
| Average RAM usage | ~2.0–2.6 GB | ~2.0–2.7 GB |

The complete benchmark graphs are available in the **images/** directory.

---

## Repository Contents

This repository includes:

- Apache Airflow DAGs
- Apache NiFi templates
- SQL scripts
- Database documentation
- Benchmark charts
- Thesis document
- ETL architecture

---

## Reproducibility

The original benchmark was executed using the infrastructure provided by CEFET-MG and the Centro de Inteligência Territorial (CIT/UFMG), including Hadoop cluster resources.

Because this infrastructure is not publicly available, the complete execution environment cannot be fully reproduced using only this repository.

This repository aims to document the project implementation, architecture and benchmark results.

---

## Future Improvements

Possible future developments include:

- Containerized local environment using Docker Compose
- Cloud-native deployment (AWS or Azure)
- Streaming ETL benchmark using Apache Kafka
- Interactive dashboards for performance analysis

---

## References

- Apache Airflow
- Apache NiFi
- Apache Spark
- PostgreSQL
- DATASUS

---

## Author

**Lucas Loscheider Reis Muniz**

Computer Engineering — CEFET-MG

- LinkedIn: https://www.linkedin.com/in/lucas-loscheider
- GitHub: https://github.com/lucaslc01
