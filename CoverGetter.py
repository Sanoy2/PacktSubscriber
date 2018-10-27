from bs4 import BeautifulSoup

class CoverGetter():
    def GetCoverLink(self, html):
        lookingFor = "dotd-main-book-image"
        soup = BeautifulSoup(html, 'html.parser')
        div = soup.find("div", {"class": lookingFor})
        soup = BeautifulSoup(str(div), 'lxml')
        return soup.find('img')['src']
