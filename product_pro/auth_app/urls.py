from django.urls import path, include
from .views import UserCreate

urlpatterns = [
    path('user/',UserCreate.as_view(), name='user'),
]