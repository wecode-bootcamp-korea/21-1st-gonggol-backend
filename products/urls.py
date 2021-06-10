from django.urls import path
from products.views import ProductMainView

urlpatterns = [
    path('', ProductMainView.as_view())
]