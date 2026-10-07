from device import Device
LIGHTBULB=[{"name":"room1","state":True,"mode":"warm","brightness":50},
        {"name":"room2","state":False,"mode":"white","brightness":100},
        {"name":"living room","state":False,"mode":"","brightness":0}]
class Lightbulb(Device):
    #Constructor
    def __init__(self, _name, _state:bool=False,_mode:str="",_brightness:float=0):
        super().__init__(_name, _state)
        self.mode=_mode
        self.brightness=_brightness
    #Turn on a lightbulb
    def turn_on(self, name):
        return super().turn_on(name, LIGHTBULB)
    #Turn off a lightbulb
    def turn_off(self, name):
        return super().turn_off(name, LIGHTBULB)
    #get light bulbs status
    def get_status(self):
        return super().get_status(LIGHTBULB)
    #configure a Lightbulb
""" 
print(LIGHTBULB)
bombilla=Lightbulb("room1")
bombilla.turn_off(bombilla.name)
print(LIGHTBULB)
lista=bombilla.get_status()
print(lista)

""" 
