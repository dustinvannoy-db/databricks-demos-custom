{{
 config(materialized = 'table', file_format = 'delta')
}}

-- notes: final user table with all information for Analysis / ML -- 
with 
    orders_stats as
    (select to_date(creation_date) creation_date,
            count(*) as order_count, 
            sum(amount) as total_amount, 
            sum(item_count) as total_item, 
             max(creation_date) as last_transaction
      from {{ref('dbt_c360_silver_orders')}} 
      group by to_date(creation_date)
    )

select *, 
       datediff(now(), creation_date) as days_since_creation,
       datediff(now(), last_activity_date) as days_since_last_activity,
       datediff(now(), last_event) as days_last_event
from orders_stats

         
         
         
         