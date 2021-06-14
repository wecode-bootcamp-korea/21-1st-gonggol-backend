from django.urls import path

from .views import CartList, CartListView

urlpatterns = [
    path('/cartlist', CartList.as_view()),
    path('/cartlistviews', CartListView.as_view()),
]