import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(receiver, body):
    from_addr = "bv6re3rctae2me6b@ethereal.email"
    login = "bv6re3rctae2me6b@ethereal.email"
    password = "WawChBJ78NbFCZCqyv"

    message = MIMEMultipart()
    message["from"] = "viagens_confirmar@email.com"
    message["to"] = ', '.join(receiver)
    message["Subject"] = "Confirmação de viagem"

    message.attach(MIMEText(body, "plain"))

    server = smtplib.SMTP("smtp.ethereal.email", 587)
    server.starttls()
    server.login(login, password)
    text = message.as_string()

    for email in receiver:
        server.sendmail(from_addr, email, text)

    server.quit()