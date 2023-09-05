with location_data as (
    select  location_id,
            iso_country_code,
            city
    from    frostbyte_tasty_bytes.raw_pos.location
)

select  *
from    location_data