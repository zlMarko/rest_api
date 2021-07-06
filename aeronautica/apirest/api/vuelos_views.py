from rest_framework import viewsets
from .serializers import *
from apirest.models import *


class VueloSViewSet(viewsets.ModelViewSet):

    serializer_class = VueloSerializer
    queryset = Vuelo.objects.all()      

