from MyMailSender import MyMailSender
from MessagesFormer import MessagesFormer
from MessageData import MessageData
import schedule
import time

class Subscriber:
    def Start(self, hour):
        schedule.every().day.at(hour).do(self.DoTheJob)
        while True:
            schedule.run_pending()
            time.sleep(1)

    def DoTheJob(self):
        messageData = self.GetMessageData()
        self.SendMail(messageData)

    def GetMessageData(self):
        messageData = MessageData()
        messageData.DownloadContent()
        return messageData

    def SendMail(self, messageData):
        mailSender = MyMailSender()
        messagesFormer = MessagesFormer()
        messages = messagesFormer.FormAllMessages(messageData)
        mailSender.Send(messages)

