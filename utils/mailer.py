import smtplib
import json
import sys
import os


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# initiate features config.
with open(resource_path("utils/config.json"), "r") as file:
    config = json.load(file)

class Mailer:
    """ Class to initiate the email alert function. """

    def __init__(self):
        self.email = config["Email_Send"]
        self.password = config["Email_Password"]
        self.port = 465
        self.server = smtplib.SMTP_SSL('smtp.gmail.com', self.port)

    def send(self, mail):
        self.server = smtplib.SMTP_SSL('smtp.gmail.com', self.port)
        self.server.login(self.email, self.password)
        # message to be sent
        SUBJECT = 'ALERT!'
        TEXT = f'People limit exceeded in your building!'
        message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
        # send the mail
        self.server.sendmail(self.email, mail, message)
        self.server.quit()
