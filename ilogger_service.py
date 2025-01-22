import os
import inspect
import requests
from typing import Optional
from dataclasses import dataclass, asdict, fields


@dataclass
class Log:
    timestamp: str
    environment: str
    service_name: str
    machine_ip: str
    type: str
    level: str
    message: str


@dataclass
class ProcessLog(Log):
    process_name: str
    function_name: str


@dataclass
class ApiLog(Log):
    method: str
    endpoint: str
    status_code: int


@dataclass
class MlLog(Log):
    step: str
    observed: Optional[str] = None
    expected: Optional[str] = None


@dataclass
class ScriptLog(Log):
    uid: str


LOG_CLASSES = []
LOG_CLASS_NAMES = []
for name, obj in inspect.getmembers(inspect.getmodule(Log)):
    if (
        inspect.isclass(obj) and issubclass(obj, Log) and obj != Log
    ):  # Exclude the base Log class itself
        LOG_CLASSES.append(obj)
        LOG_CLASS_NAMES.append(name)

BASE_FIELDS = [field.name for field in fields(Log)]  # Base class (Log) fields
TYPE_SPECIFIC_FIELDS = {}  # Get all log types and their specific fields
for cls in LOG_CLASSES:
    # Get all fields that aren't in the base Log class
    specific_fields = [
        field.name for field in fields(cls) if field.name not in BASE_FIELDS
    ]
    if specific_fields:  # Only add if there are specific fields
        TYPE_SPECIFIC_FIELDS[cls.__name__] = specific_fields


def create(log_info: Log, service_url: str) -> dict:
    """
    Send an API request to create log in the logging service.

    Parameters:
        log_info (Log): An instance of the derived classes of Log dataclass.
        service_url (str): URL for the logger service to make API calls to.

    Returns:
        dict: The response from the logging service.
    """
    if not isinstance(log_info, tuple(LOG_CLASSES)):
        raise TypeError(
            f"log_info must be an instance of one of {LOG_CLASS_NAMES} imported from {os.path.basename(__file__)}, "
            f"but got {type(log_info).__name__}"
        )

    try:
        response = requests.post(service_url, json=asdict(log_info))
        return response.json()
    except requests.RequestException as e:
        return {"error": "Failed to connect to service", "details": str(e)}
    except ValueError as e:
        return {"error": "Invalid JSON response from service", "details": str(e)}
    except Exception as e:
        return {"error": "Unexpected error occured", "details": str(e)}
