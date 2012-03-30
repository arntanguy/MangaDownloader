import Parser

class MangareaderParser(Parser):
    def __init__(self, baseUrl):
        Parser.__init__(self, baseUrl)
        print("Mangareader Parser initialized")

    def getMangaList(relativeUrl):
        """ Returns a dictionnary containing the values as key: manga name, value: manga url """
        return {'Test', 'http://test.com'}

    def getChapterList(relativeUrl):
        """ Returns a dictionnary containing the values as key: chapter title, value: chapter url """
        return {}

    def getChapterImagesUrls(relativeUrl):
        """ Returns a dictionnary containing the values as key: image name, value: image url """
        return {}

parser = MangareaderParser("http://mangareader.net")
