with country_data as (
    select *
    from {{ ref('stg_country') }}
),

location_data as (
    select *
    from {{ ref('stg_location') }}
),

location_details as (
    select      location_id,
                city_population,
                current_timestamp as timestamp
    from        location_data 
    inner join  country_data
    on          location_data.city = country_data.city 
    and         location_data.iso_country_code = country_data.iso_country_code
)

select  *
from    location_details