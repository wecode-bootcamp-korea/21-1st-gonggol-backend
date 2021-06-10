from django.urls import path
from .views      import ProductListView



urlpatterns = [
    path('/productslistview', ProductListView.as_view()),
]