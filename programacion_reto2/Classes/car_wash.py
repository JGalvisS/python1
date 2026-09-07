"""
Nombre del estudiante: Jessica Katherine Galvis Silva
Grupo: 213023_493
Programa: Ingenieria de Sistemas
Codigo fuente: autoria propia
"""
from datetime import datetime
CARS=[]
class Car_wash:
    #Constructor
    def __init__(self,_license_plate:str,_ingress_time:datetime=datetime.min,_hourly_rate:int=5000):
        self.license_plate=_license_plate
        self.ingress_time=_ingress_time
        self.hourly_rate=_hourly_rate
    #Register ingress a car 
    def ingress_register(self,ingress_time:datetime):
        found_car=False
        for i in CARS:
            if i["license_plate"] == self.license_plate:
                found_car=True
                i["ingress_time"]=ingress_time
                print(f"Ingress time: {ingress_time} has been register successful in license car plate {self.license_plate}")
        if found_car == False:
            CARS.append({"license_plate":self.license_plate,"ingress_time":ingress_time})
            print(f"Welcome to our car wash \nIngress time: {ingress_time} has been register successful in license car plate {self.license_plate}")

            
        
car1=Car_wash("SRF123")
car2=Car_wash("JDJ636")
print(CARS)
car1.ingress_register(datetime.now())
print(CARS)
car2.ingress_register(datetime.now())
car1.ingress_register(datetime.now())
print(CARS)


