import paho.mqtt.client as mqtt
from random import randrange, uniform
import time

class MQTT:
    mqtt_broker=None
    client= None
    client_Name= None


    
    def __init__(self,client_Name):
        self.mqtt_broker="broker.hivemq.com"
        self.client_Name=client_Name
        self.client=mqtt.Client(client_Name)



    def Connect_MQTT_Server(self):
        self.client.connect(self.mqtt_broker)
        print("Server connected to the ",self.client_Name)
        return True



    def Publish_Data_To_Server(self,input):
            self.client.publish(self.client_Name,input)
            print("publishing "+ str(input)+" to the topic ",self.client_Name)
            time.sleep(.2)