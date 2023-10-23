from feast import Entity
from feast.value_type import ValueType

location_entity = Entity(
    name="location",
    join_keys=["LOCATION_ID"],
    value_type=ValueType.INT32,
    description="a primary key to fetch location features"
)
