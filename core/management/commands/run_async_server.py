import uvicorn
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Run Uvicorn Server'

    def handle(self, *args, **kwargs):
        uvicorn.run('configuration.asgi:application', host="127.0.0.1", port=8000, debug=True)
