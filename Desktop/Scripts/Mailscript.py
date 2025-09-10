import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import csv

smtp_server = "smtp.gmail.com"
smtp_port = 465
sender_email = "mwamiselunani@gmail.com"
password = "maox igzg jeur iuaa"  # Consider using environment variables for security

recipients = []

# Read CSV with stripped headers
with open('C:/Users/Mwami/Desktop/Book1.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    # Strip whitespace from headers
    reader.fieldnames = [name.strip() for name in reader.fieldnames]
    for row in reader:
        recipients.append(row)

subject_template = "Hello, {Recipient}!"
body_template = """\
<html>
  <body>
    <p>Hi {Recipient},</p>
    This email contains your unique credentials...<br>
    Username: {Username} <br>
    Password: {Password} <br>
    ...
  </body>
</html>
"""

try:
    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
        server.login(sender_email, password)
        print("Connected to SMTP server successfully.")

        for recipient in recipients:
            # Use .get() to avoid KeyError if a field is missing
            recipient_email = recipient.get('Email')
            if not recipient_email:
                print(f"Skipping invalid recipient data: {recipient}")
                continue

            # Personalize subject and body
            subject = subject_template.format(**recipient)
            body = body_template.format(**recipient)

            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = recipient_email
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'html'))

            server.sendmail(sender_email, recipient_email, msg.as_string())
            print(f"Email sent to {recipient_email}")

except Exception as e:
    print(f"An error occurred: {e}")