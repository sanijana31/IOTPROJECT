import paho.mqtt.client as mqtt
from random import randrange, uniform
import time

def on_message(client, userdata, message):
	print("Received data: ",str(message.payload.decode("utf-8")))

mqtt_broker="mqtt.eclipseprojects.io"
client=mqtt.Client("SMARTPHONE")
client.connect(mqtt_broker)

client.loop_start()
client.subscribe("TEMPERATURE")
client.on_message=on_message
time.sleep(10)
client.loop_stop()