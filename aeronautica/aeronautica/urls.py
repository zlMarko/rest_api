from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apirest.api.urls')),
    path('api-vuelos/', include('apirest.api.routers')),
]
