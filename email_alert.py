import smtplib
from email.message import EmailMessage

def email_alert(body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['to'] = to

    user = "jamesdabuttler43@gmail.com"
    msg['from'] = user
    password = "bbpxrgytfxnajqzp"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    print("sent")
    server.quit()

if __name__ == '__main__':
    print("Type Message: ")
    message = input()
    email_alert(message, "jameswyllie42@gmail.com")