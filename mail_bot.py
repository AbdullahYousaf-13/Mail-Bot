import tkinter as tk
from tkinter import ttk

def submit_email():
    email = email_entry.get()
    password = password_entry.get()
    recovery = recovery_entry.get()
    vpn_or_proxy = vpn_proxy_var.get()
    
    if email and password:
        status_label.config(text=f"Email submitted successfully using {vpn_or_proxy}!", fg="green")
        # Here, you would call the backend function to store the email with the selected VPN/Proxy option
        # Example: backend_function(email, password, recovery, vpn_or_proxy)
    else:
        status_label.config(text="Email & Password are required!", fg="red")

# Initialize Tkinter window
root = tk.Tk()
root.title("Email Bot GUI")
root.geometry("400x350")

# Email Input
tk.Label(root, text="Email:").pack(pady=5)
email_entry = tk.Entry(root, width=40)
email_entry.pack()

# Password Input
tk.Label(root, text="Password:").pack(pady=5)
password_entry = tk.Entry(root, width=40, show="*")
password_entry.pack()

# Recovery Email Input
tk.Label(root, text="Recovery Email (Optional):").pack(pady=5)
recovery_entry = tk.Entry(root, width=40)
recovery_entry.pack()

# VPN or Proxy Selection
tk.Label(root, text="Select VPN or Proxy:").pack(pady=5)
vpn_proxy_var = tk.StringVar()
vpn_proxy_dropdown = ttk.Combobox(root, textvariable=vpn_proxy_var, values=["None", "VPN", "Proxy"])
vpn_proxy_dropdown.pack()
vpn_proxy_dropdown.current(0)

# Submit Button
tk.Button(root, text="Submit", command=submit_email).pack(pady=10)

# Status Label
status_label = tk.Label(root, text="", fg="blue")
status_label.pack()

# Run Tkinter Loop
root.mainloop()
