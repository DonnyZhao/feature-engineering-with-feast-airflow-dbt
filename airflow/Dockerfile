FROM quay.io/astronomer/astro-runtime:9.0.0

RUN pip install 'feast[snowflake,postgres,redis]'==0.33.1 
#typeguard dask cloudpickle

RUN python -m venv dbt_venv && source dbt_venv/bin/activate && \
pip3 install --no-cache-dir dbt-snowflake && deactivate
