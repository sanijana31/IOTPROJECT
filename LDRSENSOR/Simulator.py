import ldr_publisher as Ldr
import Mqtt_Publisher_Clint as MQTT
import time
print("Enter the maximum tolarence of the sensors")
max_res=input()
print("Enter the maximum tolarence of the sensors")
min_res=input()
ldr_sensor=Ldr.ldr(max_res,min_res)
print()
print("Enter topic name for the sensor")
client_Name=input()
ldr_data_to_mqtt=MQTT.MQTT(client_Name)
if(ldr_data_to_mqtt.Connect_MQTT_Server()):
    while True:
        cur_resistence=ldr_sensor.value_gen()
        ldr_data_to_mqtt.Publish_Data_To_Server(cur_resistence)
        time.sleep(2)
else:
    print("could not connect Mqtt")