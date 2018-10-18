from HTMLGetter import HTMLGetter
from TitleFinder import TitleFinder

class TitleGetter():
    def __init__(self):
        self.url = "https://www.packtpub.com/packt/offers/free-learning"
    
    def GetTitle(self):
        html = self.GetHtml()
        finder = TitleFinder()
        title = finder.FindTitle(html)
        return title

    
    def GetHtml(self):
        Getter = HTMLGetter()
        html = Getter.GetHTML(self.url)
        return html

