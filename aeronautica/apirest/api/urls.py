from django.urls import path
from apirest.api.api_pilotos import *
from apirest.api.api_aeronaves import *

urlpatterns = [


    path('piloto/', piloto_api_view , name = 'piloto_api'),
    path('piloto/<rut>', piloto_detail_view, name='piloto_detail_api_view'),
    path('aeronave/', aeronave_api_view, name='aeronave_api'),
    path('aeronave/<matricula>', aeronave_detail_view, name='aeronave_detail_view')
]

