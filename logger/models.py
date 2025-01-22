import os
from datetime import datetime
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()


class MongoDBManager:
    def __init__(self):
        self.client = MongoClient(os.getenv("MONGODB_URI", "mongodb://logs-db:27017/"))
        self.db = self.client["logs_db"]
        self.logs_collection = self.db["logs"]

        # Create indexes for better query performance
        self.logs_collection.create_index([("timestamp", -1)])
        self.logs_collection.create_index([("type", 1)])
        self.logs_collection.create_index([("level", 1)])
        self.logs_collection.create_index([("log_type", 1)])

    def create_log(self, log_data):
        if "timestamp" in log_data:
            log_data["timestamp"] = datetime.strptime(
                log_data["timestamp"], "%Y-%m-%dT%H:%M:%S.%f"
            )
        if "level" in log_data:
            log_data["level"] = log_data["level"].upper()
        if "method" in log_data:
            log_data["method"] = log_data["level"].upper()
        return self.logs_collection.insert_one(log_data)

    def get_logs(self, filters=None):
        query = filters or {}
        return list(self.logs_collection.find(query).sort("timestamp", -1))

    def delete_log(self, log_id):
        return self.logs_collection.delete_one({"_id": log_id})
