from feast import Entity

location_entity = Entity(
    name="location",
    join_keys=["LOCATION_ID"],
    description="a primary key to fetch location features"
)