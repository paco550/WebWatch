from celery import shared_task
import requests
from datetime import datetime
from .models import SitioWeb
import logging

logger = logging.getLogger(__name__)

@shared_task
def check_website_status(sitio_id):
    """Analiza un único sitio web por su ID y actualiza su estado en la base de datos"""
    try:
        sitio = SitioWeb.objects.get(id=sitio_id)
        
        logger.info(f"Analizando sitio web: {sitio.url}")
        inicio = datetime.now()
        
        try:
            headers = {
                'User-Agent': 'WebWath Monitoring Bot/1.0',
            }
            response = requests.get(sitio.url, timeout=10, headers=headers)
            tiempo_respuesta = (datetime.now() - inicio).total_seconds()
            
            # Actualizar información en la base de datos
            if 200 <= response.status_code < 300:
                estado = "Operativo"
            elif 300 <= response.status_code < 400:
                estado = "Redirección"
            elif 400 <= response.status_code < 500:
                estado = "Error cliente"
            elif 500 <= response.status_code < 600:
                estado = "Error servidor"
            else:
                estado = f"Código {response.status_code}"
                
            sitio.estado = estado
            sitio.tiempo_respuesta = tiempo_respuesta
            sitio.save()  # No necesitamos actualizar ultimo_chequeo ya que tiene auto_now=True
            
            logger.info(f"Sitio {sitio.url} analizado con éxito: Estado {estado}, Tiempo: {tiempo_respuesta:.2f}s")
            
            return {
                'status': estado,
                'response_time': tiempo_respuesta,
                'url': sitio.url
            }
        except requests.RequestException as e:
            # Captura errores de conexión, timeout, etc.
            sitio.estado = "Error"
            sitio.save()
            
            logger.error(f"Error al analizar sitio {sitio.url}: {str(e)}")
            
            return {
                'status': "Error",
                'error': str(e),
                'url': sitio.url
            }
    except SitioWeb.DoesNotExist:
        logger.error(f"Sitio con ID {sitio_id} no encontrado en la base de datos")
        return {'error': f"Sitio con ID {sitio_id} no encontrado"}

@shared_task
def check_all_websites():
    """Obtiene todos los sitios web de la base de datos y programa su análisis"""
    logger.info("Iniciando análisis de todos los sitios web")
    sitios = SitioWeb.objects.all()
    
    if not sitios:
        logger.warning("No hay sitios web en la base de datos para analizar")
        return {"message": "No hay sitios web para analizar"}
    
    tasks = []
    for sitio in sitios:
        task = check_website_status.delay(sitio.id)
        tasks.append(task.id)
    
    logger.info(f"Se han programado {len(tasks)} tareas de análisis")
    return {
        'message': f'Se han programado {len(tasks)} tareas de análisis',
        'task_ids': tasks
    }