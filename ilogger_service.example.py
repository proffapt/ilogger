import os
import ilogger_service as log
from datetime import datetime

service_url = os.getenv("ILOGGER_URL", "http://localhost:8001/logs/api/")

# Example for ApiLog
resp = log.create(
    log_info=log.ApiLog(
        timestamp=datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f"),
        environment="dev",
        service_name="test_service",
        machine_ip="10.105.12.5",
        type="ApiLog",
        level="INFO",
        message="Created compute environment",
        method="POST",
        endpoint="/batch/api",
        status_code=200,
    ),
    service_url=service_url
)
print(resp)

# Example for MlLog
resp = log.create(
    log_info=log.MlLog(
        timestamp=datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f"),
        environment="dev",
        service_name="test_service",
        machine_ip="10.105.12.5",
        type="MlLog",
        level="INFO",
        message="training model on 100 instances",
        step="training",
        expected="creation of model file",
        observed="model file created by the name name.cktp",
    ),
    service_url=service_url
)
print(resp)

# Example for ScriptLog
resp = log.create(
    log_info=log.ScriptLog(
        timestamp=datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f"),
        environment="dev",
        service_name="test_service",
        machine_ip="10.105.12.5",
        type="ScriptLog",
        level="INFO",
        message="terraform architecture creation triggered",
        uid="tf_create-1324234k"
    ),
    service_url=service_url
)
print(resp)
