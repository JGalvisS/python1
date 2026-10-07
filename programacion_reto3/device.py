"""
Nombre del estudiante: Jessica Katherine Galvis Silva
Grupo: 213023_493
Programa: Ingenieria de Sistemas
Codigo fuente: autoria propia
"""
class Device:
    #Constructor
    def __init__(self,_name:str,_state:bool=False):
        self.name=_name
        self.state=_state
    #Turn on a device
    def turn_on(self,name:str,device_list:list):
        state=True
        successful=False
        found_device=False
        for i in device_list:
            if i["name"]==name:
                found_device=True
            if found_device==True:
                i["state"]=state
                successful=True
            elif found_device == False:
                successful
        return successful
    #Turn off a device
    def turn_off(self,name:str,device_list:list):
        state=False
        successful=False
        found_device=False
        for i in device_list:
            if i["name"]==name:
                found_device=True
            if found_device==True:
                i["state"]=state
                successful=True
            elif found_device == False:
                successful
        return successful
    #Get status of a device
    def get_status(self,device_list:list):
        status=device_list
        return status