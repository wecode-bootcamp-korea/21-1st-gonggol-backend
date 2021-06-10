from django.urls import path

from products.views import ProductDetailView, ProductMainView

urlpatterns = [
    path('', ProductMainView.as_view()),
    path('/productdetail', ProductDetailView.as_view()),
]
