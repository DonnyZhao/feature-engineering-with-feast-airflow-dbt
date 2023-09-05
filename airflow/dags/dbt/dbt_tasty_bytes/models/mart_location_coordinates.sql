

with source_data as (
    select  location_id,
            longitude,
            latitude,
            current_timestamp as timestamp
    from frostbyte_safegraph.public.frostbyte_tb_safegraph_s
)

select  *
from    source_data