from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from apirest.api.serializers import *
from apirest.models import *
from rest_framework.decorators import api_view



@api_view(['GET', 'POST'])
def consultor_api_view(request):
    #list
    if request.method == 'GET':
        consultor = Consultor.objects.all().values('rut','nombre', 'apellido')
        consultor_serializer = ConsltorSerializer(consultor, many=True)
        return Response(consultor_serializer.data, status = status.HTTP_200_OK)
    #create
    elif request.method == 'POST':
        consultor_serializer = ConsltorSerializer(data=request.data)

        #validation
        if consultor_serializer.is_valid():
            consultor_serializer.save()
            return Response(consultor_serializer.data, status=status.HTTP_201_CREATED)

    return Response(consultor_serializer.errors,status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def consultor_detail_view(request, rut):
    #query
    consultor = Consultor.objects.filter(rut=rut).first()
    #validation
    if consultor:
        
        #retrieve 
        if request.method == 'GET':
            consultor_serializer = ConsltorSerializer(consultor)
            return Response(consultor_serializer.data, status=status.HTTP_200_OK)
        #update
        elif request.method == 'PUT':
            consultor_serializer = ConsltorSerializer(consultor, data=request.data)
            if consultor_serializer.is_valid():
                consultor_serializer.save()
                return Response(consultor_serializer.data, status.HTTP_200_OK)
            return Response(consultor_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
        #delete
        elif request.method == 'DELETE':
            consultor.delete()
            return Response({'message':'consultor elimiado'}, status=status.HTTP_200_OK)
    return Response({'message':'consutor no encontrado'}, status=status.HTTP_400_BAD_REQUEST)
