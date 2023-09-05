with country_data as (
    select      iso_country as iso_country_code,
                city,
                city_population
    from        frostbyte_tasty_bytes.raw_pos.country
)

select  *
from    country_data