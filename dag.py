from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime, timedelta

#from download-data import main

default_dag_args = {
    'owner': 'groupe5',
    'start_date': datetime.now(),
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    dag_id='iabd1_groupe5_data_pipeline_dag',
    schedule_interval=timedelta(minutes=1),
    default_args=default_dag_args
)

playlists = BashOperator(
    task_id="playlists",
    bash_command="python3 ",
    dag=dag
)

# spark_submit = BashOperator(
#     task_id = "spark_submit",
#     bash_command = "spark-submit --deploy-mode cluster --master yarn --class job.stat hdfs:///user/iabd2_group2/Stat.jar",
#     dag = dag
# )

# """ extract_data = PythonOperator(
#     task_id = "extract_data",
#     python_callable = main,
#     dag = dag
# )
