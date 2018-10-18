from html.parser import HTMLParser
import urllib.request

url = "https://www.packtpub.com/packt/offers/free-learning"

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)
        if(len(attrs) > 0):
            print("attrs:", attrs)

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        print("Encountered some data  :", data)

print(url)

fp = urllib.request.urlopen("http://www.python.org")
mybytes = fp.read()

mystr = mybytes.decode("utf8")
fp.close()

parser = MyHTMLParser()
parser.feed(mystr)

feed = '<html><head><title>Test</title></head>'  #           '<body><h1 class="fast-and-furious">Parse me!</h1></body></html>'
#parser.feed('<html><head><title>Test</title></head>'
 #           '<body><h1 class="fast-and-furious">Parse me!</h1></body></html>')
