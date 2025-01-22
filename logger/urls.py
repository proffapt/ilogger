from django.urls import path
from .views import LogsView

urlpatterns = [
    path("api/", LogsView.as_view(), name="logs"),
    path("api/<str:log_id>", LogsView.as_view(), name="log-detail"),
]
