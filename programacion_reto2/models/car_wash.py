"""
Nombre del estudiante: Jessica Katherine Galvis Silva
Grupo: 213023_493
Programa: Ingenieria de Sistemas
Codigo fuente: autoria propia
"""
from datetime import datetime,timedelta
CARS=[]
class Car_wash:
    #Constructor
    def __init__(self,_license_plate:str,_ingress_time:datetime=datetime.min,_hourly_rate:int=5000):
        self.license_plate=_license_plate
        self.ingress_time=_ingress_time
        self.hourly_rate=_hourly_rate
    #Register car ingress time  
    def ingress_register(self,ingress_time:datetime):
        successful_ingress=False
        found_car=False
        for i in CARS:
            if i["license_plate"] == self.license_plate:
                found_car=True
                i["ingress_time"]=ingress_time
                print(f"Ingress time: {ingress_time} has been register successful in car license plate {self.license_plate}.")
                successful_ingress=True
                return True
        if found_car == False:
            CARS.append({"license_plate":self.license_plate,"ingress_time":ingress_time})
            print(f"Welcome to our car wash \nIngress time: {ingress_time} has been register successful in license car plate {self.license_plate}.")
            successful_ingress=True
            return True
        elif successful_ingress==False:
            return False
        
    #Register ready car time
    def pickup_register (self, pickup_time: datetime, license_plate:str):
        found_car=False
        for i in CARS:
            if i["license_plate"]==license_plate:
                found_car=True
                i["pickup_time"]=pickup_time
                print(f"Pick up time : {pickup_time} has been register successful in car license plate {license_plate}. ")
                return found_car
        if found_car == False:
            print(f"Register pick up time unsuccessful, the car license plate {license_plate} couldn't be find.")
            return found_car
    #Calculate the charge
    def calculate_charge(self):
        enough_date=False
        for i in CARS:
            if i["license_plate"]==self.license_plate:
                if "ingress_time" in i and "pickup_time" in i:
                    enough_date=True
                    difference=i["pickup_time"] - i["ingress_time"]
                    calculate_time=difference.total_seconds()/3600
                    calculate_charge=round(calculate_time * self.hourly_rate)
                    print(f"Charge to car license plate {self.license_plate} is ${calculate_charge}")
                    return calculate_charge
        if enough_date==False:
            print(f"Cannot calculate the  charge,the car {self.license_plate} dont have registers ingress time or pick up time.")
            return False
    #get information plate
    def get_info_car(self):
        found_car=False
        for i in CARS:
            if i["license_plate"]==self.license_plate:
                found_car==True
                info_car=str
                if "ingress_time" in i and "pickup_time" in i:
                    info_car=f"The car {i["license_plate"]} has ingress {i["ingress_time"]} and exit {i["pickup_time"]}."
                    print(info_car)
                elif "ingress_time" in i:
                    info_car=f"The car {i["license_plate"]} has ingress {i["ingress_time"]}"
                    print(info_car)
                return info_car
        if found_car == False:
            print("Car information could't be find")
            return False
    #get all license registers
    def get_all_license(self):
        license_plates=[]
        for i in CARS:
            license_plates.append(i["license_plate"])
        if not license_plates:
            print("there isn't any license registered")
            return False
        print("\n".join(license_plates)) 
        return license_plates
        
"""       
car1=Car_wash("SRF123")
car2=Car_wash("JDJ636")
car3=Car_wash("PSJ455")
print(CARS)
car1.ingress_register(datetime.now())
print(CARS)
car2.ingress_register(datetime.now())
car1.ingress_register(datetime.now())
print(CARS)
car2.pickup_register(datetime.now()+timedelta(hours=3))
car3.pickup_register(datetime.now())
print(CARS)
car2.calculate_charge()
car3.calculate_charge()
print(CARS)
car3.get_licence_plate()
""" 
