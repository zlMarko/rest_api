from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-views/', include('apirest.api.urls')),
    path('api-viewsets/', include('apirest.api.routers')),
]
