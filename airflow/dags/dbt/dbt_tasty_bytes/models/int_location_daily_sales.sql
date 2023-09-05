with order_data as (
    select      *
    from        {{ ref('stg_order_header') }}
),

daily_sales as (
    select      location_id,
                date(order_ts) as business_date,
                sum(order_total) as daily_sales
    from        order_data
    group by    location_id,
                business_date
)

select      *
from        daily_sales