from rest_framework import viewsets
from .serializers import *
from apirest.models import *




class ReporteViewSet(viewsets.ModelViewSet):

    serializer_class = ReporteSerializer
    queryset = Reporte.objects.all()      

