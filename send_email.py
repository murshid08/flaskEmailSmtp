from email.mime.text import MIMEText
import smtplib

def send_email(name,email,phone):
    from_email="___email here___"
    from_paasword="___password here___"
    to_email=email
    to_name=name

    subject="help out"
    message="Hey the this is ur <strong>%s</strong>"%phone

    msg=MIMEText(message,'html')
    msg['Subjuct']=subject
    msg['to']=to_email
    msg['from']=from_email

    gmail=smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email,from_paasword)
    gmail.send_message(msg)



