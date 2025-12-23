from django.urls import path
from .views import update_location, get_location

urlpatterns = [
    path("update/", update_location),
    path("get/<str:device_id>/", get_location),
]
