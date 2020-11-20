from datetime import timedelta, datetime, date
import time
from airflow import models
from airflow import DAG
from airflow.contrib.operators.s3_to_gcs_operator import S3ToGoogleCloudStorageOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash_operator import BashOperator
from airflow.contrib.operators.gcs_to_bq import GoogleCloudStorageToBigQueryOperator
from google.cloud import bigquery
from google.oauth2 import service_account


# Update with your own config
SCHEDULE_INTERVAL = None
DAG_ID = 's3_to_gcs_to_bq_demo'
START_DATE = datetime.strptime('2020-11-17','%Y-%m-%d')
GCS_BUCKET_NAME_S3_TASK = 'gs://mybucket/myfolder/' #we are using two different operators that treat GCS file paths differently
GCS_BUCKET_NAME_BQ_TASK = 'mybucket/myfolder' #we are using two different operators that treat GCS file paths differently
DESTINATION_TABLE = 'project_name.dataset_name.table_name'
S3_BUCKET = "my_s3_bucket" # Create S3 bucket, then create IAM resourece with read access to bucket, and download access keys
AWS_CONNECTION = 'my_connection_id' #create a Connection in airflow, select S3 as connection type, and enter AWS access keys in extra section using following format - {"aws_access_key_id":"my_key", "aws_secret_access_key": "my_secret"}
GCS_BUCKET_CONNECTION = 'google_cloud_default' # Uses default connection created when you spin up Composer
BQ_CONNECTION = 'bigquery_default' # Uses default connection created when you spin up Composer
OWNER = 'john doe'
EMAIL = 'fake@email.com'

# Set default args
default_args = {
    'owner': OWNER,
    'depends_on_past': False,
    'email': EMAIL, 
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1,
    'start_date': START_DATE,
}


with DAG(DAG_ID,
        default_args=default_args,
        schedule_interval=SCHEDULE_INTERVAL
        ) as dag:

    start = DummyOperator(
        task_id='start',
        trigger_rule='all_success'
    )

    end = DummyOperator(
        task_id='end',
        trigger_rule='one_success'
    )

    # Task to copy files from S3 to GCS
    s3_email_to_gcs = S3ToGoogleCloudStorageOperator(
        task_id='s3_to_gcs',
        bucket= S3_BUCKET, 
        aws_conn_id=AWS_CONNECTION,         
        dest_gcs_conn_id= GCS_BUCKET_CONNECTION,
        dest_gcs=GCS_BUCKET_NAME_S3_TASK
    )
    s3_email_to_gcs.set_upstream(start)

    # Task to load files from GCS into BQ 
    gcs_to_bq_task = GoogleCloudStorageToBigQueryOperator(
        task_id='gcs_to_bq',
        bucket=GCS_BUCKET_NAME_BQ_TASK,
        source_objects= ['*.parquet'], # Assumes we're loading parquet files, other file types are supported
        destination_project_dataset_table=DESTINATION_TABLE, 
        source_format='parquet',
        skip_leading_rows=1,
        max_bad_records=10,
        bigquery_conn_id= BQ_CONNECTION,
        create_disposition='CREATE_IF_NEEDED', # Creates table in BQ if none is found
        write_disposition='WRITE_APPEND' 
    )
    gcs_to_bq_task.set_upstream(s3_email_to_gcs)