import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from config.settings import settings


def create_message(destinatario: str, subject: str, body: str) -> MIMEMultipart:
    msg = MIMEMultipart()
    msg["From"] = settings.EMAIL_USER
    msg["To"] = destinatario
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))
    return msg


def send_email(destinatario: str, subject: str, body: str) -> None:
    if not settings.EMAIL_USER or not settings.EMAIL_PASS:
        raise ValueError("As credenciais de e-mail não estão configuradas.")

    message = create_message(destinatario, subject, body)
    with smtplib.SMTP(settings.SMTP_SERVER, settings.SMTP_PORT) as server:
        server.starttls()
        server.login(settings.EMAIL_USER, settings.EMAIL_PASS)
        server.sendmail(settings.EMAIL_USER, destinatario, message.as_string())
