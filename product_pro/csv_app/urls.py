from django.urls import path
from .views import csv_upload_view, fetch_csv_data

urlpatterns = [
    path('csv-upload/', csv_upload_view, name='csv_upload'),
    path('fetch-csv-data/', fetch_csv_data, name='fetch_csv_data'),
]
