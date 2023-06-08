{{
 config(materialized = 'view', persist_docs={"relation": true, "columns": true})
}}

--notes: order data cleaned and anonymized for analysis -- 
select
  *,
  'yellow_json' as source
from json.`s3://one-env/dustinvannoy/nyctaxi/source/tripdata/yellow_json`