from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from apirest.api.serializers import *
from apirest.models import *
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def aeronave_api_view(request):
    # list
    if request.method == 'GET':

        aeronave = Aeronave.objects.all()
        aeronave_serializer = AeronaveSerializer(aeronave, many=True)
        return Response(aeronave_serializer.data, status=status.HTTP_200_OK)

    # create
    elif request.method == 'POST':
        aeronave_serializer = AeronaveSerializer(data=request.data)

        # validation
        if aeronave_serializer.is_valid():
            aeronave_serializer.save()
            return Response(aeronave_serializer.data, status=status.HTTP_201_CREATED)

        return Response(aeronave_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def aeronave_detail_view(request, matricula):
    # query
    aeronave = Aeronave.objects.filter(matricula=matricula).first()

    # validation
    if aeronave:
        #retrieve
        if request.method == 'GET':

            aeronave_serializer = AeronaveSerializer(aeronave)
            return Response(aeronave_serializer.data, status=status.HTTP_200_OK)
        # update
        elif request.method == 'PUT':

            aeronave_serializer = AeronaveSerializer(data=request.data)

            if aeronave_serializer.is_valid():
                aeronave_serializer.save()
                return Response(aeronave_serializer.data, status=status.HTTP_200_OK)

            return Response(aeronave_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # delete
        elif request.method == 'DELETE':

            aeronave.delete()
            return Response({'message': 'Aeronave Eliminado'}, status=status.HTTP_200_OK)
    return Response({'message': 'No se ha encontrado la aeronave'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def aeronave_available(request):

    #query
    aeronave = Aeronave.objects.all().filter(disponible = True)
    #validation
    if aeronave:
        if request.method == 'GET':
            aeronave_serializer = AeronaveAvailableSerializer(aeronave, many=True)
            return Response(aeronave_serializer.data, status=status.HTTP_200_OK)
    return Response({'message': 'error'}, status=status.HTTP_400_BAD_REQUEST)


