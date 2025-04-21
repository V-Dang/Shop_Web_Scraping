from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'admin',
    'retries': 2,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id='web_scraper',
    default_args=default_args,
    description='This is the first dag that we write',
    start_date=datetime(2024, 1, 1),
    schedule='@weekly'
) as dag:
    task1 = BashOperator(
        task_id='task1_initialize',
        bash_command='echo starting the webscraper'
    )
    task2 = BashOperator(
        task_id='task2_run_python',
        bash_command='python ../excel_web_scrape.py'
    )