from django.urls import path
from .views import all_products, product_detail

urlpatterns = [
    path('', all_products, name="products"),
    path('<product_id>', product_detail, name="product_detail"),
]
