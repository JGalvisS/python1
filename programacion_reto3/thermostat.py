"""
Nombre del estudiante: Jessica Katherine Galvis Silva
Grupo: 213023_493
Programa: Ingenieria de Sistemas
Codigo fuente: autoria propia
"""
from device import Device
from datetime import time
THERMOSTAT=[{"name":"room1","state":True,"temperature":22,"turn_on_time":time(18, 0, 0,),"turn_off_time":time(5, 0, 0,)},
        {"name":"room2","state":False,"temperature":27,"turn_on_time":time(17, 0, 0,),"turn_off_time":time(4, 0, 0,)},
        {"name":"living room","state":False,"temperature":0,"turn_on_time":"","turn_off_time":""},
        {"name":"room3","state":True,"temperature":0,"turn_on_time":"","turn_off_time":""}]
class Thermostat(Device):
    #Constructor
    def __init__(self, _name, _state = False,_temperature:float=0,_turn_on_time:time=None,_turn_off_time:time=None):
        super().__init__(_name, _state)
        self.temperature=_temperature
        self.turn_on_time=_turn_on_time
        self.turn_off_time=_turn_off_time
    #Turn on thermostat
    def turn_on(self,name:str=None):
        return super().turn_on(name,THERMOSTAT)
    #Turn off a thermostat
    def turn_off(self,name:str=None):
        return super().turn_off(name,THERMOSTAT)
    #get thermostats status
    def get_status(self):
        return super().get_status(THERMOSTAT)
    #configure thermostat
    def configure_thermostat(self):
        successful=False
        found_thermostat=False
        for i in THERMOSTAT:
            if i["name"]==self.name:
                found_thermostat=True
            if found_thermostat == True:
                if self.state != None:
                    i["state"]=self.state
                if self.temperature != None:
                    i["temperature"]=self.temperature
                if self.turn_on_time != None:
                    i["turn_on_time"]=self.turn_on_time
                if self.turn_off_time  != None:
                    i["turn_off_time"]=self.turn_off_time
                successful=True
                break
            elif found_thermostat==False:
                successful
        return successful
"""
print(THERMOSTAT)
thermostat=Thermostat("room2",None,16,time(23,0),time(5,0))
thermostat.turn_off("room1")
print(THERMOSTAT)
#lista=thermostat.get_status()
#print(lista)
"""

        
        