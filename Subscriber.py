from TitleGetter import TitleGetter
from NewMailSender import NewMailSender
import schedule
import time


class Subscriber:
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
        NewSender = NewMailSender()
        NewSender.SetAddressesByFileName("addressees.txt")
        NewSender.SetLoginDataByFileName("loginData.txt")
        NewSender.Send(title)