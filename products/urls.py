from django.urls import path

from products.views import ProductDetailView, ProductListView, ProductMainView

urlpatterns = [
    path('/<product_id>', ProductDetailView.as_view()),
    path('', ProductListView.as_view()),
    path('/main', ProductMainView.as_view()),
]
