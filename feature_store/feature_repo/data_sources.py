from feast import SnowflakeSource
import yaml 

DATABASE = yaml.safe_load(open("feature_store.yaml"))["offline_store"]["database"]
SCHEMA = "ANALYTICS"

location_sales_source = SnowflakeSource(
    database=DATABASE,
    schema=SCHEMA,
    table="MART_LOCATION_HISTORIC_SALES",
    timestamp_field="TIMESTAMP"
)

location_coordinates_source = SnowflakeSource(
    database=DATABASE,
    schema=SCHEMA,
    table="MART_LOCATION_COORDINATES",
    timestamp_field="TIMESTAMP"
)

location_population_source = SnowflakeSource(
    database=DATABASE,
    schema=SCHEMA,
    table="MART_LOCATION_POPULATION",
    timestamp_field="TIMESTAMP"
)

