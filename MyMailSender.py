import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from FileReader import FileReader
from MessagesFormer import MessagesFormer
from LoginData import LoginData

class MyMailSender:
    def Send(self, messages):
        for message in messages:
            text = message.as_string()

            messTo = message['To']
            messFrom = message['From']

            loginData = LoginData()

            session = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            session.login(loginData.GetLogin(), loginData.GetPassword())
            session.sendmail(messFrom, messTo, text)

        session.quit()

