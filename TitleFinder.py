from bs4 import BeautifulSoup

class TitleFinder():
    def FindTitle(self, html):
        lookingFor = "title-bar-title"
        soup = BeautifulSoup(html, 'html.parser')
        div = soup.find("div", {"id": lookingFor})

        soup = BeautifulSoup(str(div), 'lxml')

        title = soup.find('h1').text

        return title