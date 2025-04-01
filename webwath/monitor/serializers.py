from rest_framework import serializers
from .models import SitioWeb

class SitioWebSerializer(serializers.ModelSerializer):
    class Meta:
        model = SitioWeb
        fields = ['id', 'url', 'estado', 'tiempo_respuesta', 'ultimo_chequeo']
        read_only_fields = ['id', 'ultimo_chequeo']
        extra_kwargs = {
            'url': {'validators': []},  # Deshabilitar la validación de URL
        }