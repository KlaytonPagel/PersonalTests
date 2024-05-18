import requests
from email.message import EmailMessage
import os
import ssl
import smtplib
from dotenv import load_dotenv

# Class that sends a message to the discord server at the URL
class DiscordAlert:

    # Set up alert system with the url and header
    def __init__(self):
        load_dotenv()
        self.url = os.getenv("DISCORD_KEY")

    # Use passed in message and send the post to the server
    def send_alert(self, message):
        message = {"content": f"{message}"}
        requests.post(self.url, message)


class EmailAlert:
    def __init__(self):
        load_dotenv()

        self.mailer = EmailMessage()

        self.password = os.getenv("EMAIL_KEY")
        self.sender_email = "pagelklayton@gmail.com"

    def send_alert(self, subject, message):
        email = "pagelklayton@gmail.com"
        self.mailer["From"] = self.sender_email
        self.mailer["To"] = email
        self.mailer["Subject"] = subject
        self.mailer.set_content(message)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
            smtp.login(self.sender_email, self.password)
            smtp.sendmail(self.sender_email, email, self.mailer.as_string())
