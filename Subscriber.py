from TitleGetter import TitleGetter
from MyEmailSender import MyEmailSender
from FileReader import FileReader
import schedule
import time

class Subscriber:
    def __init__(self):
        self.Sender = MyEmailSender("loginData.txt")

    def Start(self, hour):
        schedule.every().day.at(hour).do(self.DoTheJob)
        while True:
            schedule.run_pending()
            time.sleep(1)


    def DoTheJob(self):
        title = self.GetTitle()
        self.SendMail(title)


    def GetTitle(self):
        Getter = TitleGetter()
        title = Getter.GetTitle()
        return title


    def SendMail(self, title):
        self.Sender.Send(title, "addressees.txt")