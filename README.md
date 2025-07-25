# Mail-Bot

## Project Description: 

Email Account Manager with VPN Integration

This project consists of a Python-based GUI application (mail_bot_vpn_excel.py) that:

- **Collects Email Credentials:**

  Stores email, password, recovery email (optional), and VPN/proxy preference via a user-friendly Tkinter interface.

- **Automates VPN Connectivity:**

  Integrates with Windscribe VPN (via CLI) to connect/disconnect automatically when "VPN" mode is selected.

- **Saves Data to Excel:**

  Uses openpyxl to export submitted credentials to emails.xlsx with columns: Email, Password, Recovery Email, VPN/Proxy.

## Key Features:

- **Input Validation:** Ensures mandatory fields (email/password) are provided.

- **Security:** Optional VPN/proxy selection for anonymous submissions.

- **User-Friendly:** Real-time status updates (success/error messages).

## Example Workflow:

- User submits test@example.com with VPN enabled.

- App connects to Windscribe → saves data → disconnects VPN → exports to Excel.

## Use Cases:

- Securely managing bulk email accounts.

- Testing applications with VPN-toggled credentials.

## Note: 

Storing plaintext passwords is not secure for production; consider encryption for real-world use.

## Files Summary:

- mail_bot.py: Basic email submission GUI.

- mail_bot_vpn.py: Adds VPN automation.

- mail_bot_vpn_excel.py: Full version with Excel export.

- emails.xlsx/Generated_Emails.xlsx: Sample output files.

---
