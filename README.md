# Lake-driven architecture with AWS S3 and Google Cloud

This project illustrates how to automate a Lake-driven architecture with AWS S3 and Google Cloud (GCS, BigQuery, Composer, etc.)

This example illustrates how to:
* Transfer files from S3 --> GCS (Cloud Storage) or S3 --> BigQuery (BQ)
* Automate the data pipeline with Cloud Composer (Apache Airflow)

# 0. Prerequisite

* A [GCP Project](https://cloud.google.com/resource-manager/docs/creating-managing-projects#creating_a_project) linked with a billing account (e.g., Free credits)
* A [AWS Account](https://aws.amazon.com/) linked with a payment account
* Some [parquet files](https://github.com/Teradata/kylo/tree/master/samples/sample-data/parquet) as example for the source

# 1. Implementation

* [gsutil - S3 to GCS](https://cloud.google.com/resource-manager/docs/creating-managing-projects#creating_a_project) 
* [Cloud Composer: S3 to GCS. GCS to BQ](https://cloud.google.com/resource-manager/docs/creating-managing-projects#creating_a_project)
* [Storage Transfer Service (STS) - S3 to GCS](https://cloud.google.com/resource-manager/docs/creating-managing-projects#creating_a_project) linked with a billing account (e.g., Free credits)
* [BQ Data Transfer Service (DTS) -  S3 to BQ](https://cloud.google.com/resource-manager/docs/creating-managing-projects#creating_a_project) linked with a billing account (e.g., Free credits)
