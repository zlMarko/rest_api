from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from apirest.api.serializers import *
from apirest.models import *
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def piloto_api_view(request):
    # list
    if request.method == 'GET':

        piloto = Piloto.objects.all().values('rut', 'nombre','apellido','password',)
        piloto_serializer = PilotoListSerializer(piloto, many=True)
        return Response(piloto_serializer.data, status=status.HTTP_200_OK)

    # create
    elif request.method == 'POST':
        piloto_serializer = PilotoSerializer(data=request.data)

        # validation
        if piloto_serializer.is_valid():
            piloto_serializer.save()
            return Response(piloto_serializer.data, status=status.HTTP_201_CREATED)

        return Response(piloto_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def piloto_detail_view(request, rut):
    # query
    piloto = Piloto.objects.filter(rut=rut).first()

    # validation
    if piloto:
        #retrieve
        if request.method == 'GET':

            piloto_serializer = PilotoSerializer(piloto)
            return Response(piloto_serializer.data, status=status.HTTP_200_OK)
        # update
        elif request.method == 'PUT':

            piloto_serializer = PilotoSerializer(piloto, data=request.data)

            if piloto_serializer.is_valid():
                piloto_serializer.save()
                return Response(piloto_serializer.data, status=status.HTTP_200_OK)

            return Response(piloto_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # delete
        elif request.method == 'DELETE':

            piloto.delete()
            return Response({'message': 'Piloto Eliminado'}, status=status.HTTP_200_OK)
    return Response({'message': 'No se ha encontrado el piloto'}, status=status.HTTP_400_BAD_REQUEST)
