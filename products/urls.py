from django.urls import path

from .views import ProductListView

urlpatterns = [
    path('', ProductListView.as_view()),
    
]

"""
http://:8000/products
http://:8000/products?categoryId=1&sort=-name
"""


