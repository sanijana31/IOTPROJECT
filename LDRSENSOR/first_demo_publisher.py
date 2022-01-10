import paho.mqtt.client as mqtt
from random import randrange, uniform
import time

mqtt_broker="mqtt.eclipseprojects.io"
client=mqtt.Client("TEMPERATURE")
client.connect(mqtt_broker)

while True:
	rand_number=uniform(10.0,20.0)
	client.publish("TEMPERATURE",rand_number)
	print("publishing "+ str(rand_number)+" to the topic TEMPERATURE")
	time.sleep(2)