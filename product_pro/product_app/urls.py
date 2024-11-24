from .views import (ProductCreate, ProductList, ProductDetail, ProductUpdate, ProductDelete,
                     product_list, delete_product, product_list_csv)
from django.urls import path

urlpatterns = [
    path('api/products/create/', ProductCreate.as_view(), name = 'product-create'),
    path('api/products/', ProductList.as_view(), name = 'products'),
    path('api/products/detail/<int:pk>/', ProductDetail.as_view(), name = 'products-deatil'),
    path('api/products/update/<int:pk>/', ProductUpdate.as_view(), name = 'products-update'),
    path('api/products/delete/<int:pk>/', ProductDelete.as_view(), name = 'products-delete'),

    path('products/', product_list, name='product_list'),
    path('product/delete/<int:pk>/', delete_product, name='product_delete'),
    path('products/csv/', product_list_csv, name='product_list_csv'),

]

