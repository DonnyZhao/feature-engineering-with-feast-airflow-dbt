from feast import FeatureView, Field
from feast.types import String, Int32, Float32

from data_sources import location_sales_source, location_coordinates_source, location_population_source
from entities import location_entity

sales_features = FeatureView(
    name="location_sales_features",
    entities=[location_entity],
    schema=[
        Field(name="BUSINESS_DATE", dtype=String),
        Field(name="MONTH", dtype=Int32),
        Field(name="DAY_OF_WEEK", dtype=Int32),
        Field(name="DAILY_SALES", dtype=Float32),
        Field(name="AVG_PREVIOUS_DAY_SALES", dtype=Float32),
        Field(name="AVG_L10_DAY_SALES", dtype=Float32)
    ],
    source=location_sales_source
)

coordinate_features = FeatureView(
    name="location_coordinate_features",
    entities=[location_entity],
    schema=[
        Field(name="LONGITUDE", dtype=Int32),
        Field(name="LATITUDE", dtype=Int32)
    ],
    source=location_coordinates_source
)

population_features = FeatureView(
    name="population_features",
    entities=[location_entity],
    schema=[
        Field(name="CITY_POPULATION", dtype=Int32)
    ],
    source=location_population_source
)