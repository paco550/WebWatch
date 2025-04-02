from django.core.management.base import BaseCommand
from monitor.tasks import check_all_websites

class Command(BaseCommand):
    help = 'Analiza todos los sitios web en la base de datos'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Iniciando análisis de sitios web...'))
        result = check_all_websites()
        self.stdout.write(self.style.SUCCESS(f'Análisis programado: {result["message"]}'))