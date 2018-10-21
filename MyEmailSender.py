import smtplib 
from FileReader import FileReader

class MyEmailSender:
    def __init__(self, loginDataFileName):
        loginData = self.GetLoginData(loginDataFileName)
        self.login = loginData[0]
        self.password = loginData[1]


    def Send(self, ebookTitle, addresseesFileName):
        session = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        
        messageFrom = self.login
        login = self.login
        password = self.password
        
        subject = "Packt free ebook informer"

        message = """ 
        Today's free ebook from packt: 
        %s """ % (ebookTitle)

        session.login(login, password) 

        addressees = self.GetAddressees(addresseesFileName)
        for messTo in addressees:
            emailText = """  
            From: %s  
            To: %s  
            Subject: %s

            %s
            
            """ % (messageFrom, messTo, subject, message)
            
            session.sendmail(messageFrom, messTo, emailText)
        
        session.quit()

    def GetAddressees(self, fileName):
        fileReader = FileReader()
        return fileReader.ReadLines(fileName)

    def GetLoginData(self, fileName):
        fileReader = FileReader()
        return fileReader.ReadLines(fileName)