from django.shortcuts import render
from .serializers import Product, ProductSerializer, ProductRetriveSerializer
from rest_framework import generics
#from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .pagination import CustomPagination
         
class ProductCreate(generics.CreateAPIView):
    ''' Create a Product in Product Model'''
    
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductList(generics.ListAPIView):
    ''' Retrive all Products of Product Model also custom pagination class is use 
        to retrieve 4 objects per page for goes on any page simply pass the page_no 
        value to 'page'query parameter .
    '''
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    queryset = Product.objects.all()
    serializer_class = ProductRetriveSerializer


class ProductDetail(generics.RetrieveAPIView):
    ''' Retrieve single record from databse '''

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductRetriveSerializer


class ProductUpdate(generics.UpdateAPIView):
    '''Update the record from databse by using id '''

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDelete(generics.DestroyAPIView):
    '''To delete the single record by using id '''

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer