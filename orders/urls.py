from django.urls import path

from .views import CartView

urlpatterns = [
    path('/cartview/<int:productId>', CartView.as_view()),
    path('/cartview', CartView.as_view()),
]