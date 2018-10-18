import urllib.request

class HTMLGetter():
    def GetHTML(self, url):
        return self.Mock()
        # fp = urllib.request.urlopen(url)
        # mybytes = fp.read()
        # html = mybytes.decode("utf8")
        # fp.close()
        # return html

    def Mock(self):
        return "<html><head><title>Test</title></head><body><div id=\"title-bar-title\"><h1>The Title</h1></div></body></html>"