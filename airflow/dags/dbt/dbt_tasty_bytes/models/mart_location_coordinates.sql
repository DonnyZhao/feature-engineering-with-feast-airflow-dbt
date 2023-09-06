

with source_data as (
    select  location_id,
            longitude,
            latitude,
            current_timestamp as timestamp
    from frostbyte_safegraph.public.frostbyte_tb_safegraph_s
    where location_id is not null
)

select  *
from    source_data