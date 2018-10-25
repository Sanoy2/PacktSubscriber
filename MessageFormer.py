from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class MessageFormer():
    def FormMessage(self, ebookTitle, messFrom, messTo):
        message = MIMEMultipart()
        message['From'] = messFrom
        message['To'] = messTo
        message['Subject'] = "Packthub free ebook title subscription"
        message.attach(MIMEText(self.GetHTMLConent(ebookTitle, messFrom), 'html'))
        return message

    def GetHTMLConent(self, ebookTitle, messFrom):
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
            theTitle = ebookTitle,
            email = messFrom,
            link = "https://www.packtpub.com/",
            freeEbookLink = "https://www.packtpub.com/packt/offers/free-learning"
        )
        return html