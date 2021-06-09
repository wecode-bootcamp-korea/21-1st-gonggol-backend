from django.urls import path
from .views import CartList

urlpatterns = [
    path('/cartlist', CartList.as_view()),
]