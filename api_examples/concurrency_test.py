from local_config import db_token, db_host, db_endpoint_id
import requests, json

host = db_host
warehouse_id = db_endpoint_id
token = db_token

# sql = """SELECT year(birthDate) as birthYear, count(*) AS total FROM default.people10m WHERE firstName = 'Mary' AND gender = 'F' GROUP BY birthYear ORDER BY birthYear"""
sql = 'select o_custkey, o_orderdate, o_orderpriority, c_name, c_mktsegment, o_orderstatus, sum(o_totalprice) total from orders o join customer c on o_custkey = c_custkey where c_mktsegment not in ("BUILDING", "HOUSEHOLD") group by o_custkey, o_orderdate, o_orderpriority, c_name, c_mktsegment, o_orderstatus limit 20;'

#sql = 'SELECT concat_ws('-', M.id, N.id, random()) as ID FROM range(1000) AS M, range(1000) AS N'

base_uri = f'https://{host}/api/2.0/sql/statements'
auth = ('token', token)
headers = {'Host': host, 'Content-Type': 'application/json'}
# 'Authorization': f'Bearer {dftoken}'
body = {
    'statement': 'select 1',
    'warehouse_id': 'ead10bf07050390f'
}
print(json.dumps(body))

# ,
#     'disposition': 'EXTERNAL_LINKS',
#     'format': 'ARROW_STREAM'


# 'await_result_for': {'secs': 10}
# resp = requests.request(method='POST', auth=auth, headers=headers, url=base_uri, json=json.dumps(body))

# sql_statement = "SELECT concat_ws('-', M.id, N.id, random()) as ID FROM range(1000) AS M, range(1000) AS N"
payload = json.dumps({
    "statement": 'select 1',
    "warehouse_id": warehouse_id,
    "wait_timeout": "10s",
    # "disposition": "EXTERNAL_LINKS",
    # "format": "ARROW_STREAM"
})
resp = requests.post(base_uri, auth=auth, headers=headers, data=payload)
print(resp)
print(resp.text)

## Alternative - JDBC
import JayDeBeApi



## Alternative - Python SQL Connector
#pip install databricks-sql-connector

# DATABRICKS_SERVER_HOSTNAME="e2-demo-field-eng.cloud.databricks.com"
# DATABRICKS_HTTP_PATH="/sql/1.0/warehouses/ead10bf07050390f"
# DATABRICKS_TOKEN="xxxx"
#
# from databricks import sql
# import os
# import pyspark.sql.functions
#
# with sql.connect(server_hostname=DATABRICKS_SERVER_HOSTNAME,
#                  http_path=DATABRICKS_HTTP_PATH,
#                  access_token=DATABRICKS_TOKEN) as connection:
#     with connection.cursor() as cursor:
#         cursor.execute("select * from hive_metastore.default.covid_stats limit 10")
#         result = cursor.fetchall()
#
# for row in result:
#     print(row)


