from django.shortcuts import render
from rest_framework import viewsets
from .models import SitioWeb
from .serializers import SitioWebSerializer
# Create your views here.


class SitioWebViewSet(viewsets.ModelViewSet):
    queryset = SitioWeb.objects.all()
    serializer_class = SitioWebSerializer
