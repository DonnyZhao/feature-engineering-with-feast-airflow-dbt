from feast import Entity

location_entity = Entity(
    name="location",
    join_keys=["LOCATION_ID"],
    value_type=ValueType.INT32,
    description="a primary key to fetch location features"
)
