import tkinter as tk
from tkinter import messagebox

class LoginRegisterWindow:
		def __init__(self, master):
				self.master = master
				self.master.title("Login/Register")

				self.username_var = tk.StringVar()
				self.password_var = tk.StringVar()

				self.create_widgets()

		def create_widgets(self):
				tk.Label(self.master, text="Username:").pack()
				tk.Entry(self.master, textvariable=self.username_var).pack()
				tk.Label(self.master, text="Password:").pack()
				tk.Entry(self.master, textvariable=self.password_var, show="*").pack()

				tk.Button(self.master, text="Login", command=self.login).pack()
				tk.Button(self.master, text="Register", command=self.register).pack()

		def login(self):
				# Check if username and password are valid
				if self.username_var.get() == "admin" and self.password_var.get() == "password":
						messagebox.showinfo("Login successful", "Welcome to the application!")
				else:
						messagebox.showerror("Login failed", "Invalid username or password")

		def register(self):
				register_window = tk.Toplevel(self.master)
				register_window.title("Register")

				username_var = tk.StringVar()
				password_var = tk.StringVar()
				confirm_password_var = tk.StringVar()

				tk.Label(register_window, text="Username:").pack()
				tk.Entry(register_window, textvariable=username_var).pack()
				tk.Label(register_window, text="Password:").pack()
				tk.Entry(register_window, textvariable=password_var, show="*").pack()
				tk.Label(register_window, text="Confirm Password:").pack()
				tk.Entry(register_window, textvariable=confirm_password_var, show="*").pack()

				tk.Button(register_window, text="Register", command=lambda: self.register_user(username_var.get(), password_var.get(), confirm_password_var.get())).pack()

		def register_user(self, username, password, confirm_password):
				if password != confirm_password:
						messagebox.showerror("Registration failed", "Passwords do not match")
				else:
						# Save the new user to a database or file
						messagebox.showinfo("Registration successful", f"User {username} has been registered")

root = tk.Tk()
myapp = LoginRegisterWindow(root)
myapp.master.maxsize(300, 200)

# start the program
myapp.master.mainloop()
