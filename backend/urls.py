from django.urls import path
from .views import index, detection_view

urlpatterns = [
    path("", index, name="index"),
    path("detect/", detection_view, name="detection"),
]
