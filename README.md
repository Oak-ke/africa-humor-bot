# Email Automation Script

This Python script automates the process of sending personalized emails to multiple recipients using data from a CSV file. It uses the `smtplib` library to connect to an SMTP server and send emails, and the `email` library to format the email content.

## Features

- Reads recipient data from a CSV file.
- Sends personalized emails with dynamic subject lines and HTML-formatted bodies.
- Handles missing or invalid recipient data gracefully.
- Uses secure SMTP (SSL) for email delivery.

## Prerequisites

- Python 3.x installed on your system.
- A Gmail account for sending emails.
- A CSV file containing recipient data.

## Setup

1. **Install Required Libraries**  
   This script uses Python's built-in libraries, so no additional installations are required.

2. **Prepare the CSV File**  
   The CSV file should be located at `C:/Users/Mwami/Desktop/Book1.csv` and must include the following columns:
   - `Email`: The recipient's email address.
   - `Recipient`: The recipient's name.
   - `Username`: The recipient's username.
   - `Password`: The recipient's password.

   Ensure that the column headers in the CSV file do not have leading or trailing whitespace.

3. **Update the Script**  
   - Replace the `sender_email` variable with your Gmail address.
   - Replace the `password` variable with your Gmail app password. (Do not use your Gmail account password directly. [Learn how to generate an app password](https://support.google.com/accounts/answer/185833?hl=en).)

4. **Run the Script**  
   Execute the script using Python:
   ```bash
   python Mailscript.py
