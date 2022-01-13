# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 16:23:29 2021

@author: Debopriyo
"""
import time
import paho.mqtt.client as mqtt
from random import randrange, uniform

class Proximity:
    # class attribute
    max_voltage = None
    min_voltage = None
    max_distance = None
    min_distance = None
    cur_distance = None
    intensity = None #
    
    
    # instance attribute
    def __init__(self,max_volt,min_volt,max_dis,min_dis):
        self.max_voltage =max_volt
        self.min_voltage = min_volt
        self.max_distance = max_dis
        self.min_distance = min_dis
        self.cur_voltage = None
        self.intensity = None
    
    #led sensor
    def led_output(self):
        return uniform(self.max_voltage,self.min_voltage)
        
        
    def proximity_output(self):
        led_value=self.led_output()
        #akhane vul a6e
        self.cur_distance=self.min_distance+(((self.max_distance-self.min_distance)/(self.max_voltage-self.min_voltage))*(self.max_voltage-led_value))
        #self.cur_distance=self.max_distance-(led_value-self.min_voltage)*10*constant
        return self.cur_distance
    