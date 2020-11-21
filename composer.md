# Cloud Composer: S3 to GCS & GCS to BQ

This tutorial illustrates how to automate a data pipeline with AWS S3, GCS and BQ.

[Cloud Composer](https://cloud.google.com/composer/docs) is a  managed workflow orchestration service that empowers you to author, schedule, and monitor pipelines that span across clouds and on-premises data centers. Built on the popular Apache Airflow open source project and operated using the Python programming language, Cloud Composer is free from lock-in and easy to use. Apache Airflow is an open source tool used to programatically author, schedule, and monitor workflows. 

Summary of the [Airflow concepts](https://airflow.apache.org/concepts.html#):
| Concept      | Description | 
|-----------|-------------|
| DAG | Collection of organized tasks that you schedule and run. DAGs, also called workflows, are defined in standard Python files (Directed Acyclic Graph) |
| Operator | Describes a single task in a workflow, it is usually atomic. For example, the BashOperator is used to execute bash command. |
| Task | Parameterised instance of an Operator; a node in the DAG |
| Task Instance | Specific run of a task; characterised as: a DAG, a Task, and a point in time. It has an indicative state: running, success, failed, skipped, ...

Cloud Composer workflows are comprised of DAGs (Directed Acyclic Graphs). The code shown in [s3_to_gcs_to_bq_demo_for_git.py](https://github.com/mbettan/lake-s3-gcp/blob/main/s3_to_gcs_to_bq_demo_for_git.py) is the workflow code, also referred to as the DAG.



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
- Name: my-composer
- Location: us-central1
- Zone: us-central1-a

Alternatively, you could use Cloud Shell (or SDK) to automate the provisioning:
```
gcloud composer environments create my-composer --location us-central1 --zone us-central1-a
```
### Provide permission to the Service Account

Provide to the Compute Engine default service account, configured in the previous step as service account for Cloud Composer environment, the permissions to interact with BigQuery and Cloud Storage:

- IAM & Admin --> IAM --> ADD

| Member      | Role | 
|-----------|-------------|
| project@compute.gserviceaccount.com | BigQuery Admin (or less restrictive) |


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

- Edit locally the file [s3_to_gcs_to_bq_demo_for_git.py](https://github.com/mbettan/lake-s3-gcp/blob/main/s3_to_gcs_to_bq_demo_for_git.py) with the right variables
- Upload the [s3_to_gcs_to_bq_demo_for_git.py](https://github.com/mbettan/lake-s3-gcp/blob/main/s3_to_gcs_to_bq_demo_for_git.py) to the DAG folder

## 3. Execution

- Click on "s3_to_gcs_to_bq_demo" DAG (refresh if necessary)
- Trigger the workflow by clicking on Trigger DAG --> Trigger (no configuration JSON)
- Check the workflow success in Cloud Composer
- Check the results in GCS and BigQuery





