from django.apps import AppConfig
import threading

class BarsysConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'barsys'

    def ready(self):
        """Start the MQTT listener in a separate thread."""
        # Delay the import of start_mqtt_listener to avoid early model loading
        from barsys.view_helpers import start_mqtt_listener
        threading.Thread(target=start_mqtt_listener, daemon=True).start()
        