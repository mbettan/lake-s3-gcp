# Cloud Composer: S3 to GCS. GCS to BQ

This tutorial illustrates how to automate a data pipeline with AWS S3, GCS and BQ. Cloud Composer is a  managed workflow orchestration service that empowers you to author, schedule, and monitor pipelines that span across clouds and on-premises data centers. Built on the popular Apache Airflow open source project and operated using the Python programming language, Cloud Composer is free from lock-in and easy to use. Apache Airflow is an open source tool used to programatically author, schedule, and monitor workflows. 
-  DAG - a DAG (Directed Acyclic Graph) is a collection of organized tasks that you schedule and run. DAGs, also called workflows, are defined in standard Python files
- Operator - an Operator describes a single task in a workflow

## 0. Prerequisite

* A [GCP Project](https://cloud.google.com/resource-manager/docs/creating-managing-projects#creating_a_project) linked with a billing account (e.g., Free credits)
* A [AWS Account](https://aws.amazon.com/) linked with a payment account
* Some [parquet files](https://github.com/Teradata/kylo/tree/master/samples/sample-data/parquet) as example for the source
* BigQuery, Cloud Storage API enabled
* BigQuery dataset is created

## 1. Setup Amazon Web Services

* Create a service account in AWS with the required permissions by creating a new local user account and enable AWS Programmatic Access
* Asssign AWS S3 ReadOnly Access (or less retrictive access)
* Create a S3 bucket with some [parquet files](https://github.com/Teradata/kylo/tree/master/samples/sample-data/parquet)

## 2. Setup Google Cloud

### Create Cloud Composer environment 

Open Composer service in the left navigation menu (or search bar):
Create environment with following parameters for your environment:
- Name: composer-s3
- Location: us-central1
- Zone: us-central1-a

Alternatively, you could use Cloud Shell (or SDK) to automate the provisioning:
``` gcloud composer environments create my-composer-environment --location us-central1 --zone us-central1-a ```

### Configure the prerequisites

GCP environment --> PyPI packages --> Edit

| Package name      | Extras and version | 
|-----------|-------------|
| boto3 | |
| botocore | |

### Configure the connectors

Apache Airflow --> Admin --> Connections --> Edit "aws_default"

| Entity     | Value | 
|-----------|-------------|
| Conn Id  | aws_default |
| Conn Type  | Amazon Web Service |
| Extra  | {"aws_access_key_id":"XXXXXX", "aws_secret_access_key": "XXXXXX"} |

### Customize and apply the DAG

- Edit locally the file s3_to_gcs_to_bq_demo_for_git.py with the right variables
- Upload the s3_to_gcs_to_bq_demo_for_git.py to the DAG folder

## 3. Execution

- Click on "s3_to_gcs_to_bq_demo" DAG (refresh if necessary)
- Trigger the workflow by clicking on Trigger DAG --> Trigger (no configuration JSON)
- Check the workflow success in Cloud Composer
- Check the results in GCS and BigQuery





