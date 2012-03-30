from BeautifulSoup import BeautifulSoup
import re

#doc = ['<html><head><title>Page title</title></head>',
#       '<body><p id="firstpara" align="center">This is paragraph <b>one</b>.',
#       '<p id="secondpara" align="blah">This is paragraph <b>two</b>.',
#       '</html>']
#soup = BeautifulSoup(''.join(doc))

print(soup.prettify())

class Parser:
    def __init__(self, baseUrl):
        soup = BeautifulSoup()
        self.baseUrl = baseUrl

    def getMangaList(relativeUrl):
        """ Returns a dictionnary containing the values as key: manga name, value: manga url """
        return {'Test', 'http://test.com'}

    def getChapterList(relativeUrl):
        """ Returns a dictionnary containing the values as key: chapter title, value: chapter url """
        return {}

    def getChapterImagesUrls(relativeUrl):
        """ Returns a dictionnary containing the values as key: image name, value: image url """
        return {}
