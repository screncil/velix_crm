from django.urls import path
from .views import GetAllBikes, AddBike

urlpatterns = [
    path("all", GetAllBikes.as_view()),
    path("add", AddBike.as_view())
]
