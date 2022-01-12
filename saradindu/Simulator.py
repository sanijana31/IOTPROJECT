

import Proximity_sensor as Ldr
import Mqtt_Publisher_Clint as MQTT
import time
import threading
class simulator:
    t1=None
    live_data=None
    stop_threads=None
    def simulation(self,max_res,min_res,stop):
        ldr_sensor=Ldr.ldr(max_res,min_res)
        client_Name="Ldr"
        ldr_data_to_mqtt=MQTT.MQTT(client_Name)
        if(ldr_data_to_mqtt.Connect_MQTT_Server()):
            while True:
                self.live_data=cur_resistence=ldr_sensor.value_gen()
                ldr_data_to_mqtt.Publish_Data_To_Server(cur_resistence)
                if(stop()):
                    break
        else:
            print("could not connect Mqtt")
    def start(self,max_res,min_res,stop_threads):
        self.stop_threads=stop_threads
        self.t1 = threading.Thread(target=self.simulation, args=(max_res,min_res,lambda : self.stop_threads,))
        self.t1.start()
    def stop(self,stop_threads):
        print("end")
        self.stop_threads=stop_threads
        self.t1.join()
    