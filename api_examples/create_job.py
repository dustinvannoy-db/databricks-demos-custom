import requests
import json
from config import db_token, db_host

auth = ('token', db_token)
headers = {'Host': db_host, 'Content-Type': 'application/json'}

data ={
    "name": "db_eval_parallel_test_longrunning",
    "email_notifications": {
        "no_alert_for_skipped_runs": False
    },
    "webhook_notifications": {},
    "timeout_seconds": 0,
    "max_concurrent_runs": 1,
    "tasks": [
        {
            "task_key": "task_1",
            "notebook_task": {
                "notebook_path": "/",
                "source": "WORKSPACE"
            },
            "existing_cluster_id": "",
            "timeout_seconds": 0,
            "email_notifications": {}
        },
        {
            "task_key": "task_2",
            "depends_on": [
                {
                    "task_key": "task_1"
                }
            ],
            "notebook_task": {
                "notebook_path": "/Users/dustin.vannoy@databricks.com/",
                "source": "WORKSPACE"
            },
            "existing_cluster_id": "",
            "timeout_seconds": 0,
            "email_notifications": {}
        }
    ],
    "format": "MULTI_TASK"
}


response = requests.post(f"{db_host}/api/2.1/jobs/create", auth=auth, data=json.dumps(data))
print(response.text)