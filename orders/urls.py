from django.urls import path

from .views import OrderView

urlpatterns = [
    path('/orderitem/<int:productId>', OrderView.as_view()),
    path('/orderview', OrderView.as_view()),
]