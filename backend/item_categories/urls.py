from django.urls import path
from .views import GetAllCategories

urlpatterns = [
    path("all", GetAllCategories.as_view()),
]
