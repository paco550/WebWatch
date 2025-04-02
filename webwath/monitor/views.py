from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import SitioWeb
from .serializers import SitioWebSerializer
from .tasks import check_website_status  # Importamos la tarea correcta

# Create your views here.
class SitioWebViewSet(viewsets.ModelViewSet):
    queryset = SitioWeb.objects.all()
    serializer_class = SitioWebSerializer
    
    @action(detail=True, methods=['post'])
    def monitorear(self, request, pk=None):
        """Inicia la tarea de monitoreo en Celery para un sitio específico."""
        sitio = get_object_or_404(SitioWeb, pk=pk)
        tarea = check_website_status.delay(sitio.id)  # Ejecutamos la tarea con el ID del sitio
        return Response({"message": f"Monitoreo iniciado para {sitio.url}", "task_id": tarea.id})