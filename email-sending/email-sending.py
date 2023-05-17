import smtplib, ssl
import getpass
import config

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

server.login('martinreahydroformbinemailer@gmail.com', config.EMAIL_APP_PSWD)
server.sendmail('martinreahydroformbinemailer@gmail.com', ['qianxug@gmail.com'], 'hello darkness my old friend')
server.quit()