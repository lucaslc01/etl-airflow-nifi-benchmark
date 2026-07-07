# Apache NiFi Templates

This directory contains the Apache NiFi process groups used during the benchmark.

Each flow reproduces the same ETL operations implemented in Apache Airflow, allowing a direct comparison between both tools.

## Process Groups

The project includes process groups responsible for:

- Municipalities dataset
- CBO dataset
- CID dataset
- SIGTAP dataset
- CNES dataset
- SIA dataset
- Final analytical query

## Technologies

- Apache NiFi
- PostgreSQL
- Hadoop Hive

## Purpose

These templates were developed to evaluate Apache NiFi performance regarding ETL execution time, resource consumption and workflow maintainability.
