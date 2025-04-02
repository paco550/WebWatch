from rest_framework import serializers
from .models import SitioWeb

class SitioWebSerializer(serializers.ModelSerializer):
    class Meta:
        model = SitioWeb
        fields = ['id', 'url', 'estado', 'tiempo_respuesta', 'ultimo_chequeo']
        