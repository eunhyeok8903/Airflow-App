from __future__ import annotations

import pendulum

from airflow.providers.standard.operators.bash import BashOperator
from airflow.sdk import DAG, chain


with DAG(
    dag_id="dags_bash_operator", #dag_id 랑 dag 파일명 일치하게
    schedule=None,
    # start_date=pendulum.datetime(2021, 1, 1, tz="UTC"), ##이건 세계 시간 
     start_date=pendulum.datetime(2026, 10, 1, tz="Asia/Seoul"),
    catchup=False,
    tags=["example", "example2", "example3"],
) as dag:
    bash_t1 = BashOperator(
        task_id = "bash_t1", #객체명은 여기 task id랑 동일하게 맞춰주기
        bash_command = "echo who am i"
    )
    bash_t2 = BashOperator(
        task_id = "bash_t2",
        bash_command = "echo $HOSTNAME"
    )

    bash_t1 >> bash_t2