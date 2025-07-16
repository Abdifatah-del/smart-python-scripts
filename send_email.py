import smtplib
from email.message import EmailMessage


# Create a message
msg = EmailMessage()
msg['Subject'] = 'Today's reminder'
msg['From'] = 'yourmail@gmail.com'
msg['To'] = 'receiver@gmail.com'
msg.set_content('Hi! This is an automatic reminder email from Python 😎')


# Login and send via Gmail SMTP
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login('dinmejl@gmail.com', 'app-password-here')
    smtp.send_message(msg)

print("✅ The email has been sent!")
