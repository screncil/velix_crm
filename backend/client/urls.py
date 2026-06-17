from django.urls import path
from .views import AllClientsView, AddClientView

urlpatterns = [
    path("all", AllClientsView.as_view()),
    path("add", AddClientView.as_view())
]
