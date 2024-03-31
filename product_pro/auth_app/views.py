from django.shortcuts import render
from .serializers import User, UserSerializer
from rest_framework import generics
# Create your views here.

class UserCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
