from django.shortcuts import render
from rest_framework import viewsets
from .models import SitioWeb
from .serializers import SitioWebSerializer
# Create your views here.


class SitioWebViewSet(viewsets.ModelViewSet):
    queryset = SitioWeb.objects.all()
    serializer_class = SitioWebSerializer

@action(detail=True, methods=['post'])
    def monitorear(self, request, pk=None):
        """Inicia la tarea de monitoreo en Celery para un sitio específico."""
        sitio = get_object_or_404(SitioWeb, pk=pk)
        tarea = verificar_sitio.delay(sitio.url)  # Ejecuta la tarea en segundo plano
        return Response({"message": f"Monitoreo iniciado para {sitio.url}", "task_id": tarea.id})