with order_data as (
    select      location_id,
                order_ts,
                order_total 
    from        frostbyte_tasty_bytes.raw_pos.order_header
)

select      *
from        order_data