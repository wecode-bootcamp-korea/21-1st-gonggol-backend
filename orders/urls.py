from django.urls import path

from .views import CartView

urlpatterns = [
    path('/cartview', CartView.as_view()),
]