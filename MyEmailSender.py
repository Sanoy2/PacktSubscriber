import smtplib 
from FileReader import FileReader

class MyEmailSender:
    def Send(self, title):
        session = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        
        loginData = self.GetLoginData()
        messageFrom = loginData[0]
        login = loginData[0]
        password = loginData[1]
        
        subject = "Packt free ebook informer"

        message = title
        message = """ 
        Today's free ebook from packt: 
        %s """ % (title)

        session.login(login, password) 

        addressees = self.GetAddressees()
        for messTo in addressees:
            emailText = """  
            From: %s  
            To: %s  
            Subject: %s

            %s
            
            """ % (messageFrom, messTo, subject, message)
            
            session.sendmail(messageFrom, messTo, emailText) 
        
        session.quit() 

    def GetAddressees(self):
        fileReader = FileReader()
        return fileReader.ReadLines("addressees.txt")

    def GetLoginData(self):
        fileReader = FileReader()
        return fileReader.ReadLines("loginData.txt")