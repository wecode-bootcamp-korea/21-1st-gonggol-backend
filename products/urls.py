from django.urls import path

from products.views import ProductDetailView

urlpatterns = [
    path('/productdetail', ProductDetailView.as_view()),
]
