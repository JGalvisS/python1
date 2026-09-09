
from tkinter import messagebox
from models.user import User


class User_controller:
    @staticmethod
    def create_user(username, password):
        """Create a new user."""
        if not username or not password:
            messagebox.showwarning(
                "Incomplete information",
                "Enter a username and a password."
            )
            return

        try:
            created = User.create_user(username, password)
        except Exception as error:
            messagebox.showerror("Registration error", str(error))
            return

        if created is False:
            messagebox.showerror(
                "Registration error",
                "The username already exists."
            )
            return False
        else:
            messagebox.showinfo(
                "Registration successful",
                "The user was created successfully."
            )
            return True
            


    @staticmethod
    def validate_login(username, password):
        """Validate the entered username and password."""
        if not username or not password:
            messagebox.showwarning(
                "Incomplete information",
                "Enter a username and a password."
            )
            return False

        user = User(username, password)
        valid_credentials = user.validate_user(username, password)

        if valid_credentials:
            messagebox.showinfo(
                "Validation successful",
                "The user was validated successfully."
            )
            return True

        messagebox.showerror(
            "Login error",
            "The username or password is incorrect."
        )
        return False