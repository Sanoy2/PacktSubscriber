from TitleGetter import TitleGetter
from MyMailSender import MyMailSender
from MessagesFormer import MessagesFormer
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

    def SendMail(self, ebookTitle):
        mailSender = MyMailSender()
        messagesFormer = MessagesFormer()
        messages = messagesFormer.FormAllMessages(ebookTitle)
        mailSender.Send(messages)

