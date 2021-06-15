from django.urls import path
<<<<<<< HEAD
from products.views import ProductMainView

urlpatterns = [
    path('', ProductMainView.as_view())
]
=======

from products.views import ProductDetailView

urlpatterns = [
    path('/<product_id>', ProductDetailView.as_view()),
]
>>>>>>> main
