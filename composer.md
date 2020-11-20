# Cloud Composer: S3 to GCS. GCS to BQ

This tutorial illustrates how to automate a data pipeline with AWS S3, GCS and BQ

## 0. Prerequisite

* A [GCP Project](https://cloud.google.com/resource-manager/docs/creating-managing-projects#creating_a_project) linked with a billing account (e.g., Free credits)
* A [AWS Account](https://aws.amazon.com/) linked with a payment account
* Some [parquet files](https://github.com/Teradata/kylo/tree/master/samples/sample-data/parquet) as example for the source
* BigQuery, Cloud Storage API enabled
* BigQuery dataset is created 

## 0. Setup Amazon Web Services

* Create a service account in AWS with the required permissions by creating a new local user account and enable AWS Programmatic Access
* Asssign AWS S3 ReadOnly Access (or less retrictive access)
* Create a S3 bucket with some [parquet files](https://github.com/Teradata/kylo/tree/master/samples/sample-data/parquet)

## 0. Setup Google Cloud

* Provision Cloud Composer cluster 
* Enable the prerequisites
* Customize the DAG to your environment
* Upload the DAG into the DAG folders

## 0. Execution

* Trigger the workflow in Cloud Composer
* Check the results in GCS and BigQuery





