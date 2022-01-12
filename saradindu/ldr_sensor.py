# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 16:23:29 2021

@author: Debopriyo
"""
import time
import paho.mqtt.client as mqtt
from random import randrange, uniform

class ldr:
    # class attribute
    max_resistence = None
    min_resistence = None
    cur_resistence = None#random(2.5, 10.0)
    intensity = None #
    
    
    # instance attribute
    def __init__(self,max_res,min_res):
        self.max_resistence =max_res
        self.min_resistence = min_res
        self.cur_resistence = None
        self.intensity = None
        
        
    def value_gen(self):
        intensity = uniform(2.0, 10.0)
        '''self.max_resistence = 10000
        self.min_resistence = 200'''
        self.cur_resistence = ((int(self.max_resistence) - int(self.min_resistence))/8)*intensity
        print( )
        return self.cur_resistence
        
            
         
        
'''# instantiate the class
a = ldr()

#mqtt broker
mqtt_broker="mqtt.eclipseprojects.io"

#mqtt client
client=mqtt.Client("LDR")

#connect to the broker
client.connect(mqtt_broker)

while True:
    cur_resistence=a.value_gen()
    client.publish("LDR",cur_resistence)
    print("publishing "+ str(cur_resistence)+" to the topic LDR")
    time.sleep(2)'''
    

    
    