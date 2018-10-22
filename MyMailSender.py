import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from FileReader import FileReader
from MessagesFormer import MessagesFormer

class MyMailSender:
    def __init__(self):
        self.SetLoginDataByFileName()

    def Send(self, messages):
        for message in messages:
            text = message.as_string()

            messTo = message['To']
            messFrom = message['From']

            session = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            session.login(self.login, self.password)
            session.sendmail(messFrom, messTo, text)

        session.quit()

    def SetLoginDataByFileName(self):
        fileReader = FileReader()
        loginData = fileReader.ReadLines("loginData.txt")
        self.login = loginData[0]
        self.password = loginData[1]
    