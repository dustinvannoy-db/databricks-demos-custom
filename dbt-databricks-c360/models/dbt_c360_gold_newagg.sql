{{
 config(materialized = 'table', file_format = 'delta')
}}

select to_date(creation_date) creation_date,
            count(*) as order_count,
            sum(amount) as total_amount,
            sum(item_count) as total_item,
             max(creation_date) as last_transaction
      from {{ref('dbt_c360_silver_orders')}}
      group by to_date(creation_date)