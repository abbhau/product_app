from django.urls import path
from .views import *

urlpatterns = [
    path('export_school_data/', export_school_data_to_excel, name='export_school_data'),
]
