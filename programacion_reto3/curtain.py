"""
Nombre del estudiante: Jessica Katherine Galvis Silva
Grupo: 213023_493
Programa: Ingenieria de Sistemas
Codigo fuente: autoria propia
"""
from device import Device
from datetime import time
CURTAIN=[{"name":"room1","state":True,"turn_on_time":time(7, 0, 0,),"turn_off_time":time(18, 0, 0,)},
        {"name":"room2","state":False,"turn_on_time":time(6, 0, 0,),"turn_off_time":time(17, 0, 0,)},
        {"name":"living room","state":False,"turn_on_time":"","turn_off_time":""}]
class Curtain(Device):
    #Constructor
    def __init__(self, _name, _state = False,_turn_on_time:time=None,_turn_off_time:time=None):
        super().__init__(_name, _state)
        self.turn_on_time=_turn_on_time
        self.turn_off_time=_turn_off_time
    #Open curtain
    def turn_on(self):
        return super().turn_on(CURTAIN)
    #Close curtain
    def turn_off(self):
        return super().turn_off(CURTAIN)
    #Get curtains status
    def get_status(self):
        return super().get_status(CURTAIN)
    #Configure a curtain
    def configure_curtain(self):
        successful=False
        found_curtain=False
        for i in CURTAIN:
            if i["name"]==self.name:
                found_curtain=True
            if found_curtain == True:
                i["turn_on_time"]=self.turn_on_time
                i["turn_off_time"]=self.turn_off_time
                successful=True
                break
            elif found_curtain==False:
                successful
        return successful
"""
print(CURTAIN)
curtain=Curtain("living room",None,time(10,20,00),time(13,30,00))
curtain.turn_off()
curtain.configure_curtain()
print(CURTAIN)
lista=curtain.get_status()
print(lista)
"""