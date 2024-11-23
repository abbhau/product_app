from .views import ProductCreate, ProductList, ProductDetail, ProductUpdate, ProductDelete, product_list
from django.urls import path

urlpatterns = [
    path('products/create/', ProductCreate.as_view(), name = 'product-create'),
    path('api/products/', ProductList.as_view(), name = 'products'),
    path('products/detail/<int:pk>/', ProductDetail.as_view(), name = 'products-deatil'),
    path('products/update/<int:pk>/', ProductUpdate.as_view(), name = 'products-update'),
    path('products/delete/<int:pk>/', ProductDelete.as_view(), name = 'products-update'),

    path('products/', product_list, name='product_list'),
]

