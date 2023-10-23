import os
from airflow import DAG
from airflow.decorators import task
from airflow.models import Variable
from pendulum import datetime
from cosmos import DbtTaskGroup, ProjectConfig, ProfileConfig, ExecutionConfig
from cosmos.profiles import SnowflakeUserPasswordProfileMapping
from feast.infra.offline_stores.snowflake import SnowflakeOfflineStoreConfig
from feast import RepoConfig, FeatureStore
from feast.repo_config import RegistryConfig
from feast.infra.online_stores.redis import RedisOnlineStoreConfig
from datetime import datetime


CONNECTION_ID = "sf_conn"
ACCOUNT = Variable.get("SNOWFLAKE_DEPLOYMENT_URL")
USER = Variable.get("SNOWFLAKE_USER")
PASSWORD = Variable.get("SNOWFLAKE_PASSWORD")
DATABASE = Variable.get("SNOWFLAKE_DATABASE")
WAREHOUSE = Variable.get("SNOWFLAKE_WAREHOUSE")
SCHEMA = Variable.get("SNOWFLAKE_SCHEMA")
ROLE = Variable.get("SNOWFLAKE_ROLE")
DBT_PROJECT_NAME = "dbt_tasty_bytes"
DBT_EXECUTABLE_PATH = "/usr/local/airflow/dbt_venv/bin/dbt"
DBT_ROOT_PATH = "/usr/local/airflow/dags/dbt"
DBT_PROJECT_PATH = f"{os.environ['AIRFLOW_HOME']}/dags/dbt/dbt_tasty_bytes"

profile_config = ProfileConfig(
    profile_name="default",
    target_name="dev",
    profile_mapping=SnowflakeUserPasswordProfileMapping(
        conn_id=CONNECTION_ID,
        profile_args={
            "account": ACCOUNT,
            "user": USER,
            "password": PASSWORD,
            "role": ROLE,
            "warehouse": WAREHOUSE,
            "database": DATABASE,
            "schema": SCHEMA
        },
    ),
)

execution_config = ExecutionConfig(
    dbt_executable_path=DBT_EXECUTABLE_PATH,
)

with DAG(
    dag_id="location_sales_feature_engineering",
    start_date=datetime(2023, 1, 1),
    schedule=None,
    catchup=False,
    max_active_runs=1,
) as dag:

    dbt = DbtTaskGroup(
        group_id="location_sales_features",
        project_config=ProjectConfig(DBT_PROJECT_PATH),
        profile_config=profile_config,
        execution_config=execution_config
    )

    @task()
    def feast_materialize(data_interval_start=None, data_interval_end=None):
        repo_config = RepoConfig(
            registry = RegistryConfig(
                registry_type="sql",
                path="postgresql://postgres:mysecretpassword@docker.for.mac.localhost:55001/feast",
            ),
            project="tasty_bytes_feature_store",
            provider="local",
            offline_store=SnowflakeOfflineStoreConfig(
                account=ACCOUNT,
                user=USER,
                password=PASSWORD,
                role=ROLE,
                warehouse=WAREHOUSE,
                database=DATABASE,
                schema_=SCHEMA,
            ),
            online_store=RedisOnlineStoreConfig(connection_string="docker.for.mac.localhost:6379"),
            entity_key_serialization_version=2,
        )
        os.environ["NO_PROXY"] = "*"
        store = FeatureStore(config=repo_config)

        store.materialize(data_interval_start, data_interval_end)

    data_interval_start = datetime.strptime('2021-01-01T00:00:00', '%Y-%m-%dT%H:%M:%S')
    data_interval_end = datetime.now()

    dbt >> feast_materialize(data_interval_start=data_interval_start, data_interval_end=data_interval_end)
    
