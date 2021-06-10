from django.urls import path

from products.views import ProductDetailView

urlpatterns = [
    path('/product/<product_id>', ProductDetailView.as_view()),
]
