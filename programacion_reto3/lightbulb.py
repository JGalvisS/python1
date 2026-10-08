"""
Nombre del estudiante: Jessica Katherine Galvis Silva
Grupo: 213023_493
Programa: Ingenieria de Sistemas
Codigo fuente: autoria propia
"""
from device import Device
LIGHTBULB=[{"name":"room1","state":True,"mode":"warm","brightness":50},
        {"name":"room2","state":False,"mode":"white","brightness":100},
        {"name":"living room","state":False,"mode":"","brightness":0},
        {"name":"room3","state":True,"mode":"","brightness":0}]
class Lightbulb(Device):
    #Constructor
    def __init__(self, _name, _state:bool=False,_mode:str="",_brightness:float=None):
        super().__init__(_name, _state)
        self.mode=_mode
        self.brightness=_brightness
    #Turn on a lightbulb
    def turn_on(self,name:str=None):
        return super().turn_on(name,LIGHTBULB)
    #Turn off a lightbulb
    def turn_off(self,name:str=None):
        return super().turn_off(name,LIGHTBULB)
    #get light bulbs status
    def get_status(self):
        return super().get_status(LIGHTBULB)
    #configure a Lightbulb
    def configure_lightbulb(self):
        successful=False
        found_lightbulb=False
        for i in LIGHTBULB:
            if i["name"]==self.name:
                found_lightbulb=True
            if found_lightbulb==True:
                if self.state != None:
                    i["state"]=self.state
                if self.mode != None:
                    i["mode"]=self.mode
                if self.brightness != None:
                    i["brightness"]=self.brightness
                successful=True
                break
            elif found_lightbulb==False:
                successful
        return successful
            
"""
print(LIGHTBULB)
bombilla=Lightbulb("living room")
#bombilla.turn_off()
bombilla.configure_lightbulb()
print(LIGHTBULB)
lista=bombilla.get_status()
print(lista)
"""