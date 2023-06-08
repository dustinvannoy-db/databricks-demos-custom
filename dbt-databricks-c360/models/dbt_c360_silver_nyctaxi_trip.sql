{{
 config(materialized = 'table', file_format = 'delta', persist_docs={"relation": true, "columns": true})
}}

-- notes: user data cleaned and anonymized for analysis -- 
select
    *
    ,regexp_replace(substring(tpep_pickup_datetime,1,7), '-', '_') as pickup_date
    ,to_date(tpep_pickup_datetime, "yyyy-MM-dd HH:mm:ss") as pickup_timestamp
    ,to_date(tpep_dropoff_datetime, "yyyy-MM-dd HH:mm:ss") as dropoff_timestamp
from {{ref('dbt_c360_tmp_vw_nyctaxi_trip')}}