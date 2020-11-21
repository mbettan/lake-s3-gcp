# Lake-driven architecture with AWS S3 and Google Cloud

This project illustrates how to automate a Lake-driven architecture with AWS S3 and Google Cloud (GCS, BigQuery, Composer, etc.)

This example illustrates how to:
* Ingest parquet files from S3 --> GCS (Cloud Storage) or S3 --> BigQuery (BQ)
* Automate the data pipeline with Cloud Composer (Apache Airflow)

## 0. Definition

| Name      | Description | 
|-----------|-------------|
| BQ DTS | BigQuery Data Transfer Service automates data movement into BigQuery on a scheduled, managed basis. Your analytics team can lay the foundation for a BigQuery data warehouse without writing a single line of code.
| STS | Import online data from cloud sources into Cloud Storage and set up a recurring transfer schedule. Transfer data within Cloud Storage from one bucket to another.
| gsutil | gsutil is a Python application that lets you access Cloud Storage from the command line. 
| Cloud Composer | A managed workflow orchestration service built on Apache Airflow.
| BigQuery | BigQuery is a fully-managed, serverless data warehouse that enables scalable analysis over petabytes of data. It is a Platform as a Service that supports querying using ANSI SQL.
| S3 | Amazon Simple Storage Service is an Object Storage service, often used in Data Lake architecture
| GCS | Google Cloud Storage is an Object Storage service, often used in Data Lake architecture


## 1. Prerequisite

* A [GCP Project](https://cloud.google.com/resource-manager/docs/creating-managing-projects#creating_a_project) linked with a billing account (e.g., Free credits)
* A [AWS Account](https://aws.amazon.com/) linked with a payment account
* Some [parquet files](https://github.com/Teradata/kylo/tree/master/samples/sample-data/parquet) as example for the source

## 2. Implementation

* [gsutil - S3 to GCS](https://cloud.google.com/resource-manager/docs/creating-managing-projects#creating_a_project) 
* [Cloud Composer: S3 to GCS. GCS to BQ](https://github.com/mbettan/lake-s3-gcp/blob/main/composer.md)
* [Storage Transfer Service (STS) - S3 to GCS](https://cloud.google.com/resource-manager/docs/creating-managing-projects#creating_a_project)
* [BQ Data Transfer Service (DTS) -  S3 to BQ](https://cloud.google.com/resource-manager/docs/creating-managing-projects#creating_a_project)
