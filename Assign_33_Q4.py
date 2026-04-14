# Write a Python program to send an email with an attachment. The program should take the sender's email address, recipient's email address, subject, body of the email, and the file path of the attachment as input from the user. Use the smtplib library to send the email.

import smtplib
from email.message import EmailMessage

def send_email(sender, password, receiver, logfile):
    msg = EmailMessage()
    msg['Subject'] = "System Report"
    msg['From'] = sender
    msg['To'] = receiver
    msg.set_content("Attached is system log file.")

    with open(logfile, 'rb') as f:
        msg.add_attachment(f.read(), maintype='application', subtype='octet-stream', filename=logfile)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender, password)
        smtp.send_message(msg)