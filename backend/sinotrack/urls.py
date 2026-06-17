from django.urls import path
from .views import GetAllSinotracksAPI, GetAvailableSinotracks, CreateSinotrackView

urlpatterns = [
    path("all", GetAllSinotracksAPI.as_view()),
    path("available", GetAvailableSinotracks.as_view()),
    path("add", CreateSinotrackView.as_view())
]
