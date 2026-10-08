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
    @staticmethod
    def configure_curtain(name:str,state:bool=None,turn_on_time_h:int=None,turn_on_time_m:int=None,turn_off_time_h:int=None,turn_off_time_m:int=None):
        try:
            turn_off_time=None
            turn_on_time=None
            if turn_on_time_h != None and turn_on_time_m!= None:
                if 0 <= turn_on_time_h <= 23 and 0 <= turn_on_time_m <= 59:
                    turn_on_time=time(turn_on_time_h,turn_on_time_m)
            if turn_off_time_h != None and turn_off_time_m!= None:
                if  0 <= turn_off_time_h <= 23 and 0 <= turn_off_time_m <= 59:
                    turn_off_time=time(turn_off_time_h,turn_off_time_m)
            new_curtain=Curtain(name,state,turn_on_time,turn_off_time)
            new_curtain.configure_curtain()
        except Exception as error:
            messagebox.showerror("Error", "The curtain configure couldn't be completed")
        else:
            messagebox.showinfo("The curtain configure successful",f"The  {name} curtain was configured successfully")
    #Configure a lightbulb
    @staticmethod
    def configure_lightbulb(name:str,state:bool=None,mode:str=None,brightness:float=None):
        try:
            validate_mode=None
            validate_brightness=None
            if mode == "white" or mode == "warm":
                validate_mode=mode
            if brightness != None:
                if 0 <= brightness<=100:
                    validate_brightness=brightness 
            new_lightbulb=Lightbulb(name,state,validate_mode,validate_brightness)
            new_lightbulb.configure_lightbulb()
        except Exception as error:
            messagebox.showerror("Error", "The lightbulb configure couldn't be completed")
        else:
            messagebox.showinfo("The lightbulb configure successful",f"The {name} lightbulb was configured successfully")
    #Configure a thermostat
    @staticmethod
    def configure_thermostat (name:str,state:bool=None,temperature:float=None,turn_on_time_h:int=None,turn_on_time_m:int=None,turn_off_time_h:int=None,turn_off_time_m:int=None):
        try:
            turn_off_time=None
            turn_on_time=None
            validate_temperature=None
            if turn_on_time_h != None and turn_on_time_m!= None:
                if 0 <= turn_on_time_h <= 23 and 0 <= turn_on_time_m <= 59:
                    turn_on_time=time(turn_on_time_h,turn_on_time_m)
            if turn_off_time_h != None and turn_off_time_m!= None:
                if  0 <= turn_off_time_h <= 23 and 0 <= turn_off_time_m <= 59:
                    turn_off_time=time(turn_off_time_h,turn_off_time_m)
            if temperature != None:
                if 0 <= temperature<=35:
                    validate_temperature=temperature 
            new_thermostat=Thermostat(name,state,validate_temperature,turn_on_time,turn_off_time)
            new_thermostat.configure_thermostat()
        except Exception as error:
            messagebox.showerror("Error", "The thermostat configure couldn't be completed")
        else:
            messagebox.showinfo("The thermostat configure successful",f"The {name} thermostat was configured successfully")
    
                

            
#Central_controller.turn_on_all()
#Central_controller.turn_off_all()
#Central_controller.configure_curtain("room3",None,None,None,14,5)
#Central_controller.configure_lightbulb("room3",None,"warm",80)
#Central_controller.configure_thermostat ("room3",None,None,None,None,21,58)
#Central_controller.get_status_all()