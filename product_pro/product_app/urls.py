from .views import (ProductCreate, ProductList, ProductDetail, ProductUpdate, ProductDelete,
                     product_list, delete_product, product_list_csv, product_create_view,
                 product_update_view, brand_list_api, generate_reportlab_pdf_response)
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
    path('products/pdf/', generate_reportlab_pdf_response, name = 'product_list_pdf'),

    path('product/create/', product_create_view, name='product_create'),
    path('product/<int:pk>/update/', product_update_view, name='product_update'),

    path('brands/', brand_list_api, name='brand_list_api'),

]

