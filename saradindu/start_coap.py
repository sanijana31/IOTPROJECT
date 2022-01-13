import Proximity_sensor as sensor
import asyncio
import client_put as coap_c
max_volt=input()
min_volt=input()
max_dis=input()
min_dis=input()
def coap(max_volt,min_volt,max_dis,min_dis):
    proximity_sensor=sensor.Proximity(int(max_volt),int(min_volt),int(max_dis),int(min_dis))
    while True:
        p_dis=proximity_sensor.proximity_output()
        asyncio.get_event_loop().run_until_complete(coap_c.main(p_dis))
coap(max_volt,min_volt,max_dis,min_dis)