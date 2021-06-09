from django.urls import path
from .views import JoinIn, LogIn

urlpatterns = [
    path('/joinin', JoinIn.as_view()),
    path('/login', LogIn.as_view()),
]