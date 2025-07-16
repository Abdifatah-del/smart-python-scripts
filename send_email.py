import smtplib
from email.message import EmailMessage

# Skapa ett meddelande
msg = EmailMessage()
msg['Subject'] = 'Dagens påminnelse'
msg['From'] = 'dinmejl@gmail.com'
msg['To'] = 'mottagare@gmail.com'
msg.set_content('Hej! Detta är ett automatiskt påminnelsemejl från Python 😎')

# Logga in och skicka via Gmail SMTP
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login('dinmejl@gmail.com', 'app-lösenord-här')
    smtp.send_message(msg)

print("✅ Mejlet har skickats!")
