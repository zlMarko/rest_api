from django.urls import path
from apirest.api.api_pilotos import *
from apirest.api.api_aeronaves import *
from apirest.api.api_consultor import *
urlpatterns = [


    path('piloto/', piloto_api_view , name = 'piloto_api'),
    path('piloto/<rut>', piloto_detail_view, name='piloto_detail_api_view'),
    path('aeronave/', aeronave_api_view, name='aeronave_api'),
    path('aeronave/<matricula>', aeronave_detail_view, name='aeronave_detail_view'),
    path('aeronave-disponible/',aeronave_available, name='aeronave_available' ),
    path('consultor/',consultor_api_view, name='consultor_api' ),
    path('consultor/<rut>',consultor_detail_view, name='consultor_detail_view' )
]

