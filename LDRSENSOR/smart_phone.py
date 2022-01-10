import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
	print("Received data: ",str(message.payload.decode("utf-8")))

mqtt_broker="broker.hivemq.com"
client=mqtt.Client("SMARTPHONE")
client.connect(mqtt_broker)

client.loop_start()
client.subscribe("Ldr")
client.on_message=on_message
time.sleep(1000)
client.loop_stop()