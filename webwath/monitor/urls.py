from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SitioWebViewSet

router = DefaultRouter()
router.register(r'sitios', SitioWebViewSet)

urlpatterns = [
    path('', include(router.urls)),
]