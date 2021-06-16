from django.urls import path

from products.views import ProductDetailView, ProductListView

urlpatterns = [
    path('/<product_id>', ProductDetailView.as_view()),
    path('', ProductListView.as_view()),
]

