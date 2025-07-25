import tkinter as tk
from tkinter import ttk
import os
import time
import openpyxl

# List to store submitted emails
email_data = []

def connect_vpn():
    """Connect to Windscribe VPN using the best available server."""
    status_label.config(text="Connecting to VPN...", fg="blue")
    root.update()
    os.system('"C:\\Program Files\\Windscribe\\windscribe.exe" connect best')
  # Uses Windscribe CLI
    time.sleep(5)  # Allow time for connection
    status_label.config(text="Connected to VPN!", fg="green")
    root.update()

def disconnect_vpn():
    """Disconnect from Windscribe VPN."""
    status_label.config(text="Disconnecting VPN...", fg="blue")
    root.update()
    os.system('"C:\\Program Files\\Windscribe\\windscribe.exe" disconnect') # Uses Windscribe CLI
    time.sleep(3)
    status_label.config(text="VPN Disconnected.", fg="red")
    root.update()

def submit_email():
    """Collects email details and processes them."""
    email = email_entry.get()
    password = password_entry.get()
    recovery = recovery_entry.get()
    vpn_or_proxy = vpn_proxy_var.get()
    
    if vpn_or_proxy == "VPN":
        connect_vpn()

    if email and password:
        email_data.append([email, password, recovery, vpn_or_proxy])
        status_label.config(text=f"Email submitted successfully using {vpn_or_proxy}!", fg="green")
    else:
        status_label.config(text="Email & Password are required!", fg="red")

    if vpn_or_proxy == "VPN":
        disconnect_vpn()

def save_to_excel():
    """Saves collected email data to an Excel file."""
    if not email_data:
        status_label.config(text="No data to save!", fg="red")
        return

    # Create a new workbook and sheet
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Emails"

    # Write headers
    sheet.append(["Email", "Password", "Recovery Email", "VPN/Proxy"])

    # Write data
    for row in email_data:
        sheet.append(row)

    # Save file
    workbook.save("emails.xlsx")
    status_label.config(text="Emails saved to emails.xlsx!", fg="green")

    import subprocess
    subprocess.run(["start", "emails.xlsx"], shell=True)


# Initialize Tkinter window
root = tk.Tk()
root.title("Email Bot GUI")
root.geometry("400x400")

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

# Save to Excel Button
tk.Button(root, text="Save to Excel", command=save_to_excel).pack(pady=10)

# Status Label
status_label = tk.Label(root, text="", fg="blue")
status_label.pack()

# Run Tkinter Loop
root.mainloop()
