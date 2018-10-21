import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from FileReader import FileReader


class MyMailSender:
    def Send(self, ebookTitle):
        for address in self.addresses:
            htmlContent = self.GetHTMLConent(ebookTitle)
            message = self.GetMessage(address, htmlContent)
            text = message.as_string()

            session = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            session.login(self.login, self.password)
            session.sendmail(self.login, address, text)

        session.quit()

    def GetMessage(self, address, htmlContent):
        message = MIMEMultipart()
        message['From'] = self.login
        message['To'] = address
        message['Subject'] = "Packthub free ebook title subscription"
        message.attach(MIMEText(htmlContent, 'html'))
        return message

    def GetHTMLConent(self, ebookTitle):
        html = """
        <html>
            <head>
            </head>
            <body>
                <div>
                    <h1> {theTitle} </h1>
                    <h3> Is today's free ebook on <a href="{link}"> Packthub </a></h3>
                    <br>
                    <h2>
                        Get this ebook <a href="{freeEbookLink}">here</a>
                    </h2>
                </div>
                <br>
                <br>
                <p>
                    If you want to cancel this subscription please contact me: {email}
                </p>
                <p>
                    I am going to attach free ebook's cover soon :)
                </p>
            </body>
        </html>
        """.format(
            theTitle=ebookTitle,
            email=self.login,
            link="https://www.packtpub.com/",
            freeEbookLink="https://www.packtpub.com/packt/offers/free-learning"
        )
        return html

    def SetAddressesByFileName(self, addresseesFileName):
        fileReader = FileReader()
        self.addresses = fileReader.ReadLines(addresseesFileName)

    def SetLoginDataByFileName(self, loginDataFilename):
        fileReader = FileReader()
        loginData = fileReader.ReadLines(loginDataFilename)
        self.login = loginData[0]
        self.password = loginData[1]

    def PrintAddresses(self):
        for address in self.addresses:
            print(address)
