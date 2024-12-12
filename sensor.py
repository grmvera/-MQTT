import paho.mqtt.client as mqtt
import json
import time
from datetime import datetime

# Configuracion del broker
broker = "localhost"
port = 1883
topic = "home/light_sensor"


client = mqtt.Client()
client.connect(broker, port)

while True:
    data = {
        "device_id": "5ee9df89-a719-4e9a-ac54-84b9c3096f40",
        "event_time": str(datetime.now()),
        "value": 40, #cambiar el valor para ver si esta prendido o apagado mayor a 50 apaga la luz menor enciende la luz
        "accuracy": 0.98
    }
    client.publish(topic, json.dumps(data))
    print(f"Datos enviados: {data}")
    time.sleep(5)  # Enviar cada 5 segundos
