# ETL Benchmark: Apache Airflow vs Apache NiFi

> Performance benchmark of Apache Airflow and Apache NiFi for large-scale ETL pipelines using public Brazilian healthcare datasets from DATASUS.

---

## Overview

This repository contains the source code, documentation and results of my undergraduate thesis in Computer Engineering at **CEFET-MG**.

The objective of this project was to compare two of the most widely used Data Engineering tools for ETL workflows:

- Apache Airflow
- Apache NiFi

The comparison was performed using real public healthcare datasets from DATASUS, evaluating execution time, CPU usage, memory consumption, maintainability and scalability.

---

## Objectives

- Compare Apache Airflow and Apache NiFi
- Build equivalent ETL pipelines
- Process large public datasets
- Measure execution time
- Measure CPU usage
- Measure RAM consumption
- Evaluate maintainability and scalability

---

## Technologies

| Category | Technologies |
|-----------|-------------|
| Programming | Python, SQL |
| Databases | PostgreSQL, Hadoop Hive |
| ETL | Apache Airflow, Apache NiFi |
| Big Data | Apache Spark |
| Infrastructure | Docker, Linux |
| Version Control | Git, Bitbucket |

---

## Dataset

The experiments used public Brazilian healthcare datasets.

Main sources:

- DATASUS
- CNES
- SIGTAP
- CID
- Brazilian Municipalities

Approximately **42 million healthcare records** were processed during the benchmark.

---

## Architecture

> Architecture diagram coming soon.

---

## Project Structure

```text
etl-airflow-nifi-benchmark
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
```

---

## ETL Workflow

The benchmark evaluated the entire ETL lifecycle.

1. Data extraction
2. Data cleaning
3. Data transformation
4. Data integration
5. Data loading
6. SQL analytics
7. Performance monitoring

---

## Performance Results

The experiments were executed multiple times under the same environment.

### Average Execution Time

| Tool | Average Time |
|------|-------------:|
| Apache Airflow | 01:41:14 |
| Apache NiFi | 00:39:00 |

---

### Resource Consumption

| Metric | Airflow | NiFi |
|--------|---------:|------:|
| CPU Usage | ~3–4% | ~4–5% |
| RAM Usage | ~2.0–2.6 GB | ~2.0–2.7 GB |

---

## Key Findings

- Apache NiFi achieved the lowest execution time.
- Apache Airflow provided superior workflow orchestration and maintainability.
- Both tools are suitable for enterprise ETL pipelines depending on project requirements.

---

## Repository Contents

This repository includes:

- ETL source code
- Airflow DAGs
- NiFi templates
- SQL scripts
- Documentation
- Performance results
- Architecture diagrams

---

## Reproducibility

The original benchmark was executed using the infrastructure provided by CEFET-MG and the Centro de Inteligência Territorial (CIT/UFMG), including Hadoop cluster resources.

Because this infrastructure is not publicly available, the complete execution environment cannot be fully reproduced using only this repository.

The purpose of this repository is to document the project architecture, implementation, methodology and benchmark results.

---

## Future Improvements

- Dockerized local environment
- Cloud deployment
- Apache Kafka integration
- Real-time ETL benchmark
- Power BI dashboard

---

## References

- Apache Airflow Documentation
- Apache NiFi Documentation
- Apache Spark Documentation
- PostgreSQL Documentation
- DATASUS

---

## Author

**Lucas Loscheider Reis Muniz**

Computer Engineering — CEFET-MG

LinkedIn:
https://www.linkedin.com/in/lucas-loscheider
