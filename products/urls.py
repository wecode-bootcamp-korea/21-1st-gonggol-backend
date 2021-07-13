from django.urls import path

from products.views import ProductAPIView, ProductAPIDetailView

urlpatterns = [
    # path('/<int:product_id>', ProductDetailView.as_view()),
    # path('', ProductListView.as_view()),
    # path('/main', ProductMainView.as_view()),
    path('/products', ProductAPIView.as_view()),
    path('/products/<int:product_id>', ProductAPIDetailView.as_view()),
]
