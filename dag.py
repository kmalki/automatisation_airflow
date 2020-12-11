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

get_playlists = BashOperator(
    task_id="get_playlists",
    bash_command="mkdir raw_data; mkdir raw_data/playlists; "
                 "python3 /root/airflow/dags/groupe5/automatisation_airflow/python_script/get_playlists_tracks.py; "
                 "HADOOP_USER_NAME=groupe5 hdfs dfs -put -f raw_data/playlists /user/groupe5/raw_data/ ",
    dag=dag
)

get_tracks_artists = BashOperator(
    task_id="get_tracks_artists",
    bash_command="mkdir raw_data; mkdir raw_data/albums; "
                 "python3 /root/airflow/dags/groupe5/automatisation_airflow/python_script/get_tracks_popularity_by_artist.py; "
                 "HADOOP_USER_NAME=groupe5 hdfs dfs -put -f raw_data/albums /user/groupe5/raw_data/ ",
    dag=dag
)

spark_playlists = BashOperator(
    task_id="spark_playlists",
    bash_command="HADOOP_CONF_DIR=/etc/hadoop/conf HADOOP_USER_NAME=groupe5 spark-submit --deploy-mode cluster --master yarn --class Main "
                 "/root/airflow/dags/groupe5/automatisation_airflow/spark_jar/spotify_playlists_ingestion_2.12-1.0.jar ",
    dag=dag
)

spark_tracks_artists = BashOperator(
    task_id="spark_tracks_artists",
    bash_command="HADOOP_CONF_DIR=/etc/hadoop/conf HADOOP_USER_NAME=groupe5 spark-submit --deploy-mode cluster --master yarn --class Main "
                 "/root/airflow/dags/groupe5/automatisation_airflow/spark_jar/spotify_albums_ingestion_2.12-1.0.jar ",
    dag=dag
)

# get_playlists >> get_tracks_artists >> spark_playlists >> spark_tracks_artists
spark_playlists >> spark_tracks_artists