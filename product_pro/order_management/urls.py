from .views import (AddProductView,UpdateProductView, product_list_api)
from django.urls import path

urlpatterns = [
    path('add/products/', AddProductView.as_view(), name = 'add_products'),
    path('update/products/<int:pk>/', UpdateProductView.as_view(), name = 'update_products'),

    path('products/', product_list_api, name='product_list_api'),
]

