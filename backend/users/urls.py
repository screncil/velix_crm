from django.urls import path
from .views import RegisterView, UserMeView

urlpatterns = [
    path("register/", RegisterView.as_view()),
    path("me/", UserMeView.as_view())
]
