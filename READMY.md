📌 **Documentación del Proyecto: Plataforma de Monitorización Web y Ciberseguridad**

**1️⃣ Introducción**

- **Descripción:**
  Una plataforma que permite monitorizar sitios web en busca de caídas, errores SEO, problemas de rendimiento y vulnerabilidades de seguridad.
- **Objetivo:**
  Desarrollar una herramienta útil para empresas de desarrollo web, SEO y ciberseguridad, proporcionando análisis en tiempo real y alertas automáticas.

**2️⃣ Funcionalidades principales**

- **💡 Módulo 1: Monitorización de disponibilidad**
  - ✅ Detectar si un sitio web está caído (ping + respuesta HTTP).
  - ✅ Medir tiempos de carga y uptime histórico.
  - ✅ Notificaciones cuando una web deje de responder.
- **🔍 Módulo 2: Análisis de SEO y rendimiento**
  - ✅ Comprobación de etiquetas title, meta, h1, alt en imágenes.
  - ✅ Análisis de velocidad de carga con Lighthouse o WebPageTest.
  - ✅ Detección de enlaces rotos.
- **🛡️ Módulo 3: Seguridad y detección de amenazas**
  - ✅ Detección de headers de seguridad mal configurados (X-Frame-Options, CSP).
  - ✅ Integración con Google Safe Browsing para detectar phishing.
  - ✅ Análisis de certificados SSL (vigencia, emisor, cifrado).
- **🚨 Módulo 4: Alertas y reportes**
  - ✅ Notificaciones por email o Telegram en caso de problemas.
  - ✅ Panel de control con gráficos sobre el estado de los sitios.
  - ✅ Exportación de informes de análisis en PDF.

**3️⃣ Tecnologías a utilizar**

- 📌 **Back-end:** Django + Django REST Framework.
- 📌 **Tareas en segundo plano:** Celery + Redis.
- 📌 **Análisis SEO y rendimiento:** BeautifulSoup, Lighthouse API.
- 📌 **Seguridad:** Requests + Google Safe Browsing API.
- 📌 **Front-end:** Django Templates o React/HTMX.
- 📌 **Base de datos:** PostgreSQL o SQLite para desarrollo.
- 📌 **Notificaciones:** Twilio (SMS) / SMTP (Email) / Telegram Bot.

**4️⃣ Plan de desarrollo por fases**

- **🔹 Fase 1: Configuración inicial**
  - ✅ Crear el proyecto Django.
  - ✅ Configurar Celery para tareas en segundo plano.
  - ✅ Definir modelos de base de datos.
- **🔹 Fase 2: Monitorización de disponibilidad**
  - ✅ Script para hacer peticiones HTTP y guardar resultados.
  - ✅ Crear API para obtener el estado de los sitios web.
  - ✅ Integrar Celery para chequeos automáticos.
- **🔹 Fase 3: Análisis SEO y rendimiento**
  - ✅ Implementar rastreo con BeautifulSoup para etiquetas HTML.
  - ✅ Medir velocidad de carga con Lighthouse API.
  - ✅ Guardar datos en la base de datos y mostrar en el dashboard.
- **🔹 Fase 4: Seguridad y alertas**
  - ✅ Análisis de headers de seguridad.
  - ✅ Comprobación de phishing con Google Safe Browsing API.
  - ✅ Notificaciones por email y Telegram cuando haya problemas.
- **🔹 Fase 5: Dashboard y reportes**
  - ✅ Crear interfaz gráfica para visualizar datos.
  - ✅ Integrar gráficos con Chart.js o Recharts.
  - ✅ Generar informes PDF con resultados.
