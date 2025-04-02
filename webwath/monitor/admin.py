from django.contrib import admin
from .models import SitioWeb
from .tasks import check_website_status

@admin.register(SitioWeb)
class SitioWebAdmin(admin.ModelAdmin):
    list_display = ('url', 'estado', 'tiempo_respuesta', 'ultimo_chequeo')
    list_filter = ('estado',)
    search_fields = ('url',)
    actions = ['analizar_seleccionados']
    
    def analizar_seleccionados(self, request, queryset):
        for sitio in queryset:
            check_website_status.delay(sitio.id)
        self.message_user(request, f"Se han programado {queryset.count()} análisis de sitios web.")
    analizar_seleccionados.short_description = "Analizar sitios web seleccionados"