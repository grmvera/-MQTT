import paho.mqtt.client as mqtt
import json

# Configuracion del broker
broker = "localhost"
port = 1883
topic = "home/light_sensor"


def on_message(client, userdata, msg):
    data = json.loads(msg.payload)
    value = data["value"]
    accuracy = data["accuracy"]

    if value < 50 and accuracy > 0.9:
        print("Encendiendo las luces...")
    else:
        print("Apagando las luces...")

# Configura MQTT
client = mqtt.Client(protocol=mqtt.MQTTv311)
client.on_message = on_message
client.connect(broker, port)

# Suscripcion
client.subscribe(topic)
client.loop_forever()
