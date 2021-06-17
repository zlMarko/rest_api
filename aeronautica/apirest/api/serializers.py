from rest_framework import serializers
from apirest.models import *
from apirest.api import sha1_generator


class PilotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Piloto
        fields = '__all__'

    def create(self, validated_data):

        piloto = Piloto(**validated_data)
        a = sha1_generator.get_hash(validated_data['password'])
        piloto.password = a
        piloto.save()
        return piloto



class PilotoListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Piloto
        fields = '__all__'

    def to_representation(self, instance):

        data = super().to_representation(instance)
        return{
            'rut':instance['rut'],
            'nombre':instance['nombre'],
            'apellido':instance['apellido'],
            'password':instance['password'],
        }


class AeronaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aeronave
        fields = '__all__'



class VueloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vuelo
        fields = '__all__'




