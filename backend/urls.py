from django.urls import path
from .views import detection_view

urlpatterns = [
    path("detect/", detection_view, name="detection"),
]
