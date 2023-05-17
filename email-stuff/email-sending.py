import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import config

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

senderEmail = 'martinreahydroformbinemailer@gmail.com'
receiverEmail = 'richardmiao1111@gmail.com'
password = config.EMAIL_APP_PSWD

message = MIMEMultipart("alternative")
message["Subject"] = "I am a nice-looking email"
message["From"] = senderEmail
message["To"] = receiverEmail

body = """\hello my friend... uwu... meow~ RICHARD I AM NOT BAD AT CODING LOOK THE EMAIL IS SENDING"""

message.attach(MIMEText(body, 'plain'))

server.login('martinreahydroformbinemailer@gmail.com', config.EMAIL_APP_PSWD)
server.sendmail('martinreahydroformbinemailer@gmail.com', receiverEmail, message.as_string())
server.quit()