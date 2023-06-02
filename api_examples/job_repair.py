from local_config import db_token, db_host, db_endpoint_id
import json
import requests

host = db_host
warehouse_id = db_endpoint_id
token = db_token

# Repair run
# https://docs.databricks.com/api/azure/workspace/jobs/repairrun
base_uri = f'https://{host}/api/2.1/jobs/runs/repair'

auth = ('token', token)
headers = {'Host': host, 'Content-Type': 'application/json'}

body = {
    "rerun_all_failed_tasks": "true",
    "run_id": 162777397
    # ,"repair_id":
    # ,"dbt_commands": []
}
print(json.dumps(body))

payload = json.dumps(body)
resp = requests.post(base_uri, auth=auth, headers=headers, data=payload)
if resp.status_code >= 400:
    raise ValueError(f"Response indicates error - Status was {resp}, message: {resp.text}")
print(resp.text)