# feast_airflow_dbt_demo
# TODO: make README better/more-coherent

This demo you have docker desktop, because we are using astronomer to spin up airflow

1. Create a demo Snowflake account with ACCOUTNADMIN privileges 

(a) Follow the tasty bytes tutorial to load tasty bytes data into your Snowflake account. https://quickstarts.snowflake.com/guide/tasty_bytes_introduction/index.html#0
(b) Bring in the geo spatial data that we will use to enhance our tasty bytes data. https://quickstarts.snowflake.com/guide/tasty_bytes_zero_to_snowflake_geospatial/#2
(c) enable anaconda access ? 

2. First run the following commands to set up your virtual environment 
- conda create --name feast_on_snowflake --override-channels -c https://repo.anaconda.com/pkgs/snowflake python=3.10 numpy pandas
- pip install 'feast[snowflake, redis]'==0.33.1 dbt-snowflake==1.6.2

3. activate your conda environemnt conda activate feast_on_snowflake

3. Create the feast repo using the command 
- feast init tasty_bytes_feature_store -t snowflake

4. Install the astro cli (https://docs.astronomer.io/astro/cli/install-cli?tab=mac#install-the-astro-cli) and create an Astro project 
- cd airflow 
- astro dev init 

5. Initiate a dbt project inside the folder /airflow/dags/dbt and use the ANALYTICS schema
- cd airflow/dags


6. add the following environment variables to your environment for 
a. feast to connect to the Snowflake offline store.
```
export SNOWFLAKE_DEPLOYMENT_URL="[YOUR DEPLOYMENT]
export SNOWFLAKE_USER="[YOUR USER]
export SNOWFLAKE_PASSWORD="[YOUR PASSWORD]
export SNOWFLAKE_ROLE="[YOUR ROLE]
export SNOWFLAKE_WAREHOUSE="[YOUR WAREHOUSE]
export SNOWFLAKE_DATABASE="[YOUR DATABASE]
```
b. add the same variables to a .env file in the airflow repo that astronomer created for the astronomer environment to use
```
SNOWFLAKE_DEPLOYMENT_URL="[YOUR DEPLOYMENT]
SNOWFLAKE_USER="[YOUR USER]
SNOWFLAKE_PASSWORD="[YOUR PASSWORD]
SNOWFLAKE_ROLE="[YOUR ROLE]
SNOWFLAKE_WAREHOUSE="[YOUR WAREHOUSE]
SNOWFLAKE_DATABASE="[YOUR DATABASE]
```


7. - mkdir dbt
- dbt init Create the dbt project with models and run dbt run to see that everything works 

7. Now that the final mart models are in Snowflake, we will create our feature repository. Navigate to the tasty_bytes_feature_store/feature_repo folder
- remove the driver_repo.py demo file that comes with every feature store file
- Update the feature_store.yaml file to use Redis as your online store and (maybe? Postgres as your registry)
- add a Dockerfile in the feature_repo for feast
- add a docker_compose file in the tasty_bytes_feature_store directory that spins up a redis server, a postgres server to act as the registry, and a feature server using the Dockerfile you just created

8. In feast there are four classes we need to be aware of:
- data sources
- entities
- features
- feature_services

9. run `Feast Apply` which will scan all your python files for the features we've defined and deploy all the infrastructure needed in your offline feature store.

10. Now we will create an airflow pipeline that will orchestrate the data from raw staging tables to final data models with features materialized in our online and offline data source
- Create a dag that runs the dbt project with cosmos. 
- In that dag, add a step after the dbt run task for feast materialization.


11. Update the packages.txt with gcc
python3-dev, 
requirements.txt with astronomer-cosmos[dbt-snowflake]==1.0.5
snowflake-connector-python
snowflake-sqlalchemy
apache-airflow-providers-snowflake, 
and Dockerfile with RUN pip install 'feast[snowflake,redis]'==0.33.1 typeguard dask cloudpickle

12. Create a feature engineering pipeline from raw staging table -> data marts (via dbt) and materializing the features into the online and offline store via Feast

13. Spin up the feature store with the command 
docker-compose -f docker-compose-feast.yml up

14. Finally, spin up airflow with the command astro dev start 
Go to Admin -> Connections and create a new Snowflake connection using the same name (sf_conn) specified in the airflow pipeline. 
Run the pipeline. 

