from django.core.management.base import BaseCommand
from barsys.view_helpers import start_mqtt_listener

class Command(BaseCommand):
    help = 'Start the MQTT listener for product price updates'

    def handle(self, *args, **kwargs):
        start_mqtt_listener()
        