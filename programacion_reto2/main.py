"""
Nombre del estudiante: Jessica Katherine Galvis Silva
Grupo: 213023_493
Programa: Ingenieria de Sistemas
Codigo fuente: autoria propia
"""
import tkinter as tk
from tkinter import ttk

from controllers.car_wash_controller import Car_wash_controller
from controllers.user_controller import User_controller

def validate_login():
    """Validate credentials and open the main screen."""
    username = username_entry.get().strip()
    password = password_entry.get()

    valid_credentials = User_controller.validate_login(
        username,
        password
    )

    if valid_credentials:
        login_frame.pack_forget()
        main_frame.pack(fill="both", expand=True)
        clear_login_fields()

def create_user():
    """Send the entered data to the user controller."""
    created=User_controller.create_user(
        username_entry.get().strip(),
        password_entry.get()
    )
    if created:
        clear_login_fields()
    
def clear_login_fields():
    """Clear the login input fields."""
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

def get_plate():
    """Return the entered license plate."""
    return plate_entry.get().strip().upper()


def show_registered_cars():
    """Request all registered cars from the controller."""
    Car_wash_controller.get_cars_register()


def register_car():
    """Send the entered plate to the controller."""
    Car_wash_controller.register_car(get_plate())


def register_car_exit():
    """Send the entered plate to the controller."""
    Car_wash_controller.register_exit(get_plate())


def calculate_car_charge():
    """Request the charge for the entered plate."""
    Car_wash_controller.calculate_charge(get_plate())


def show_car_information():
    """Request information about the entered car."""
    Car_wash_controller.get_information_car(get_plate())
#--------

root = tk.Tk()
root.title("Fast Car Wash")
root.geometry("430x520")
root.resizable(False, False)


# Login interface.
login_frame = ttk.Frame(root, padding=30)

ttk.Label(
    login_frame,
    text="System Login",
    font=("Arial", 20, "bold")
).pack(pady=20)

ttk.Label(login_frame, text="Username").pack(anchor="w")
username_entry = ttk.Entry(login_frame)
username_entry.pack(fill="x", pady=5)

ttk.Label(login_frame, text="Password").pack(anchor="w")
password_entry = ttk.Entry(login_frame, show="*")
password_entry.pack(fill="x", pady=5)


ttk.Button(
    login_frame,
    text="Login",
    command=validate_login
).pack(fill="x", pady=10)

ttk.Button(
    login_frame,
    text="Create user",
    command=create_user

).pack(fill="x")

# Main car wash interface.
main_frame = ttk.Frame(root, padding=20)

ttk.Label(
    main_frame,
    text="Car Wash Control",
    font=("Arial", 18, "bold")
).pack(pady=10)

ttk.Label(
    main_frame,
    text="Our price is the best $5000COP a hour",
    font=("Arial", 12)
).pack(pady=10)


ttk.Label(main_frame, text="License plate").pack(anchor="w")
plate_entry = ttk.Entry(main_frame)
plate_entry.pack(fill="x", pady=3)

ttk.Button(
    main_frame,
    text="Plates registered",
    command=show_registered_cars
).pack(fill="x", pady=10)

ttk.Button(
    main_frame,
    text="Register car entry",
    command=register_car
).pack(fill="x", pady=10)


ttk.Button(
    main_frame,
    text="Register car exit",
    command=register_car_exit
).pack(fill="x", pady=10)

ttk.Button(
    main_frame,
    text="Calculate car charge to pay",
    command=calculate_car_charge
).pack(fill="x", pady=10)

ttk.Button(
    main_frame,
    text="Car information",
    command=show_car_information
).pack(fill="x", pady=10)



# The application starts with the login screen.
login_frame.pack(fill="both", expand=True)
root.mainloop()

