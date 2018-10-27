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
        messages = self.FormMessages(messageData)
        self.SendMail(messages)

    def GetMessageData(self):
        messageData = MessageData()
        messageData.DownloadContent()
        return messageData

    def FormMessages(self, messageData):
        messagesFormer = MessagesFormer()
        messages = messagesFormer.FormAllMessages(messageData)
        return messages

    def SendMail(self, messages):
        mailSender = MyMailSender()
        mailSender.Send(messages)

