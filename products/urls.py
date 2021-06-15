from django.urls import path

from products.views import ProductDetailView, ProductMainView

urlpatterns = [
    path('/<product_id>', ProductDetailView.as_view()),
    path('', ProductMainView.as_view())
]