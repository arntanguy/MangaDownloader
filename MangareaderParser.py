from Parser import Parser
from Network import Network
from BeautifulSoup import BeautifulSoup

class MangareaderParser(Parser):
    def __init__(self, baseUrl):
        Parser.__init__(self, baseUrl)
        print("Mangareader Parser initialized")

    def getMangaList(self, relativeUrl):
        """ Returns a dictionnary containing the values as key: manga name, value: manga url """
        html = self.network.getUrlContentUtf8("http://www.mangareader.net/alphabetical")
        #self.baseUrl+relativeUrl)

        self.soup = BeautifulSoup(html)
        self.soup.findAll('ul')
        print (self.soup.prettify())
        return {'Test', 'http://test.com'}

    def getChapterList(self, relativeUrl):
        """ Returns a dictionnary containing the values as key: chapter title, value: chapter url """
        return {}

    def getChapterImagesUrls(self, relativeUrl):
        """ Returns a dictionnary containing the values as key: image name, value: image url """
        return {}

parser = MangareaderParser("www.mangareader.net/")
parser.getMangaList("alphabetical")

