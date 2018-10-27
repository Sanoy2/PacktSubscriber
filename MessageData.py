from HTMLGetter import HTMLGetter
from TitleGetter import TitleGetter
from CoverGetter import CoverGetter

class MessageData():
    def __init__(self):
        self.title = ""
        self.coverSrc = ""

    def DownloadContent(self):
        htmlGetter = HTMLGetter()
        html = htmlGetter.GetHTML()

        titleGetter = TitleGetter()
        self.title = titleGetter.GetTitle(html)

        coverSrcGetter = CoverGetter()
        self.coverSrc = coverSrcGetter.GetCoverLink(html)

