import urllib.request


class HTMLGetter():
    def __init__(self):
        self.url = "https://www.packtpub.com/packt/offers/free-learning"

    def GetHTML(self):
        # return self.Mock()  # comment to turn mocking html off
        fp = urllib.request.urlopen(self.url)
        mybytes = fp.read()
        html = mybytes.decode("utf8")
        fp.close()
        return html

    def Mock(self):
        return "<html><head><title>Test</title></head><body><div id=\"title-bar-title\"><h1>The Title</h1></div></body></html>"
