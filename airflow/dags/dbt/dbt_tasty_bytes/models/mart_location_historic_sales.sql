with daily_sales as (
    select      *
    from        {{ ref('int_location_daily_sales') }}
),

historic_sales as (
    select      location_id,
                business_date,
                month(business_date) as month,
                dayofweekiso(business_date) as day_of_week,
                daily_sales,
                avg(daily_sales) over (
                    partition by location_id
                    order by business_date
                    rows between unbounded preceding and 1 preceding 
                ) as avg_previous_day_sales,
                avg(daily_sales) over (
                    partition by location_id
                    order by business_date
                    rows between 10 preceding and 1 preceding
                ) as avg_l10_day_sales,
                current_timestamp as timestamp
    from        daily_sales
)

select      *
from        historic_sales
where       avg_previous_day_sales is not null