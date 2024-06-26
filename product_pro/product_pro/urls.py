
from django.contrib import admin
from django.urls import path, include
#from rest_framework.authtoken import views
from rest_framework_simplejwt.views import token_obtain_pair,token_refresh

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('product_app.urls')),
    path('', include('auth_app.urls')),
    #path('tokens/', views.obtain_auth_token),
    path('generatetoken/',token_obtain_pair),
    path('tokenrefresh/',token_refresh)
]
