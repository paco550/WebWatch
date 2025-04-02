# webwath/celery.py
import os
from celery import Celery

# Establece la variable de entorno para que Celery sepa dónde encontrar la configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webwath.settings') # ¡Reemplaza 'webwath' si es necesario!

# Crea la instancia de Celery
# ¡Reemplaza 'webwath' si es necesario!
app = Celery('webwath')

# Carga la configuración de Celery desde el archivo settings.py de Django.
# El namespace 'CELERY' significa que todas las configuraciones de Celery en settings.py
# deben empezar con CELERY_ (ej. CELERY_BROKER_URL)
app.config_from_object('django.conf:settings', namespace='CELERY')

# Descubre automáticamente archivos tasks.py en todas las apps listadas en INSTALLED_APPS
app.autodiscover_tasks()

# Opcional: Define una tarea de prueba aquí si quieres
@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')