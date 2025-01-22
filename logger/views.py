from bson import ObjectId
from datetime import datetime
from rest_framework import status
from .models import MongoDBManager
from rest_framework.views import APIView
from rest_framework.response import Response
from ilogger_service import LOG_CLASS_NAMES, BASE_FIELDS, TYPE_SPECIFIC_FIELDS


class LogsView(APIView):
    def __init__(self):
        super().__init__()
        self.mongo_manager = MongoDBManager()

    def post(self, request):
        try:
            log_data = request.data

            # Validate log type
            if log_data.get("type") not in LOG_CLASS_NAMES:
                return Response(
                    {"error": f"Invalid log type: {log_data.get('type')}"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            required_fields = BASE_FIELDS + TYPE_SPECIFIC_FIELDS[log_data["type"]]
            missing_fields = [
                field for field in required_fields if field not in log_data
            ]
            if missing_fields:
                return Response(
                    {"error": f"Missing required fields: {', '.join(missing_fields)}"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            result = self.mongo_manager.create_log(log_data)
            return Response(
                {"id": str(result.inserted_id)}, status=status.HTTP_201_CREATED
            )

        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def get(self, request):
        try:
            filters = {} 
            # NOTE: Filters must be case-insensitive

            # Parse query parameters
            if request.query_params.get("type"):
                log_type = request.query_params["type"]
                if log_type not in LOG_CLASS_NAMES:
                    return Response(
                        {"error": f"Invalid log type: {log_type}. Valid types are {LOG_CLASS_NAMES}"},
                        status=status.HTTP_400_BAD_REQUEST,
                    )
                filters["type"] = {"$regex": f"^{log_type}$", "$options": "i"}
            if request.query_params.get("level"):
                filters["level"] = {"$regex": f"^{request.query_params['level']}$", "$options": "i"}

            # Date range filters
            if request.query_params.get("start_date"):
                try:
                    start_date = datetime.strptime(
                        request.query_params["start_date"], "%Y-%m-%dT%H:%M:%S"
                    )
                    filters["timestamp"] = {"$gte": start_date}
                except ValueError as e:
                    return Response(
                        {"error": f"Invalid start_date format: {str(e)}"},
                        status=status.HTTP_400_BAD_REQUEST,
                    )
            if request.query_params.get("end_date"):
                try:
                    end_date = datetime.strptime(
                        request.query_params["end_date"], "%Y-%m-%dT%H:%M:%S"
                    )
                    if "timestamp" in filters:
                        filters["timestamp"]["$lte"] = end_date
                    else:
                        filters["timestamp"] = {"$lte": end_date}
                except ValueError as e:
                    return Response(
                        {"error": f"Invalid end_date format: {str(e)}"},
                        status=status.HTTP_400_BAD_REQUEST,
                    )

            # Specific filters based on log type
            for _type in LOG_CLASS_NAMES:
                specific_fields = TYPE_SPECIFIC_FIELDS.get(_type, [])
                for field in specific_fields:
                    if request.query_params.get(field):
                        value = request.query_params[field]
                        # Case-insensitive search filters
                        filters[field] = {"$regex": f"^{value}$", "$options": "i"}

            logs = self.mongo_manager.get_logs(filters)

            # Convert ObjectId to string for JSON serialization
            for log in logs:
                log["_id"] = str(log["_id"])

            return Response(logs)

        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def delete(self, request, log_id):
        try:
            result = self.mongo_manager.delete_log(ObjectId(log_id))
            if result.deleted_count:
                return Response(status=status.HTTP_204_NO_CONTENT)
            return Response(
                {"error": "Log not found"}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
