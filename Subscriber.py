from TitleGetter import TitleGetter
from MyMailSender import MyMailSender
from MessagesFormer import MessagesFormer
from HTMLGetter import HTMLGetter
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
        htmlGetter = HTMLGetter()
        html = htmlGetter.GetHTML()
        Getter = TitleGetter()
        title = Getter.GetTitle(html)
        return title

    def SendMail(self, ebookTitle):
        mailSender = MyMailSender()
        messagesFormer = MessagesFormer()
        messages = messagesFormer.FormAllMessages(ebookTitle)
        mailSender.Send(messages)

