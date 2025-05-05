import threading
from barsys.view_helpers import start_mqtt_listener

def on_starting(server):
    """Start the MQTT listener in the Gunicorn master process."""
    print("Starting MQTT listener...")
    threading.Thread(target=start_mqtt_listener, daemon=True).start()
    