"""
Nombre del estudiante: Jessica Katherine Galvis Silva
Grupo: 213023_493
Programa: Ingenieria de Sistemas
Codigo fuente: autoria propia
"""
from tkinter import messagebox
from datetime import datetime, timedelta
from models.car_wash import Car_wash

class Car_wash_controller:

    @staticmethod
    def register_car(plate):
        """Register a car using the Fast Car Wash."""
        if not plate: 
            messagebox.showwarning(
                "Incomplete information",
                "Ingres a license plate."
            )
            return
        
        try:
            new_car=Car_wash(plate)
            new_car.ingress_register(datetime.now())
        except Exception as error:
            messagebox.showerror("Registration error", "Registration error")
        else:
            messagebox.showinfo(
                "Registration successful",
                f"Car {plate} was registered successfully."
            )
    @staticmethod        
    def register_exit(plate):
        """Register the selected car exit."""
        if not plate: 
            messagebox.showwarning(
                "Incomplete information",
                "Ingres a license plate."
            )
            return
        try:
            car_exit=Car_wash(plate)
            car_exit.pickup_register(datetime.now(),plate)
            #car_exit.pickup_register(datetime.now()+timedelta(hours=10),plate)
        except Exception:
            messagebox.showerror(
                "Registration exit car time error",
                f"the car license plate {plate} couldn't be find ." 
            )
        else:
            messagebox.showinfo(
                "Registration exit car time was successful",
                f"Car {plate} has registered successfully its exit car time."
            )
    @staticmethod    
    def calculate_charge(plate):
        """calculate its payment."""
        if not plate: 
            messagebox.showwarning(
                "Incomplete information",
                "Ingres a license plate."
            )
            return
        try:
            car_charge=Car_wash(plate)
            charge=car_charge.calculate_charge()
            if charge == False:
                raise error
        except Exception as error:
            messagebox.showerror(
                "Charge calculate error",
                f"the car license plate {plate} couldn't be find or it hasn't a exit car register." 
            )
        else:
            messagebox.showinfo(
                "Calculate car charge was successful",
                f"Car {plate} should pay ${charge}."
            )
    @staticmethod        
    def get_information_car(plate): 
        """Get information car."""
        if not plate: 
            messagebox.showwarning(
                "Incomplete information",
                "Ingres a license plate."
            )
            return
        try:
            car=Car_wash(plate)
            info_car=car.get_info_car()
            if info_car  is False:
                raise error
        except Exception as error:
            messagebox.showerror(
                "Information license plate dont find",
                f"The license {plate} isn't registered ."
                )
            return
        else:
            messagebox.showinfo("Car information", info_car)
    @staticmethod
    def get_cars_register():
        """Get each license register"""
        try:
            register=Car_wash("000")
            list_register=register.get_all_license()
            if list_register is False:
                raise ValueError
        except Exception:
                messagebox.showinfo(
            "Registered cars",
            "There are no registered license plates."
        )
        else:
            messagebox.showinfo(
            "Registered cars",
            "\n".join(list_register)
        )