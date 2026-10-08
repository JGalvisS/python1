"""
Nombre del estudiante: Jessica Katherine Galvis Silva
Grupo: 213023_493
Programa: Ingenieria de Sistemas
Codigo fuente: autoria propia
"""
from tkinter import messagebox
from datetime import time
from lightbulb import Lightbulb
from curtain import Curtain
from thermostat import Thermostat

class Central_controller:
    #Turn on all devices
    @staticmethod
    def turn_on_all():
        try:
            new_curtain=Curtain("")
            new_lightbulb=Lightbulb("")
            new_thermostat=Thermostat("")
            new_curtain.turn_on()
            new_lightbulb.turn_on()
            new_thermostat.turn_on()
        except Exception as error:
            messagebox.showerror("Error", "Turn on devices error")
        else:
            messagebox.showinfo("Turn on successful", "Turn on devices successfully")
    #Turn off all devices
    @staticmethod
    def turn_off_all():
        try:
            new_curtain=Curtain("")
            new_lightbulb=Lightbulb("")
            new_thermostat=Thermostat("")
            new_curtain.turn_off()
            new_lightbulb.turn_off()
            new_thermostat.turn_off()
        except Exception as error:
            messagebox.showerror("Error", "Turn off devices error")
        else:
            messagebox.showinfo("Turn off successful", "Turn off devices successfully")
    #Get status all devices
    @staticmethod
    def get_status_all():
        try:
            new_curtain=Curtain("")
            new_lightbulb=Lightbulb("")
            new_thermostat=Thermostat("")
            curtain_list=new_curtain.get_status()
            lightbulb_list=new_lightbulb.get_status()
            thermostat_list=new_thermostat.get_status()
            all_lists=[curtain_list,lightbulb_list,thermostat_list]
            final_message=""
            tittles=["\n 🪟 CURTAINS\n","\n 💡 LIGHT BULBS\n","\n 🌡️ THERMOSTAT\n"]
            counter=0
            for i in all_lists:
                final_message+=tittles[counter]
                counter+=1
                for j in i:
                    final_message +="•"
                    for key, value in j.items():
                        final_message +=f"{key}:{value}    "
                    final_message+="\n\n"
        except Exception as error:
            messagebox.showerror("Error", "System status error")
        else:
            messagebox.showinfo("System status successful", 
                                f"System status devices successfully:\n{final_message}")
    #Configure a curtain

            
#Central_controller.turn_on_all()
#Central_controller.turn_off_all()
Central_controller.get_status_all()