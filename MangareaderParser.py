#!/usr/bin/python
# -*- coding: utf-8 -*-

from Parser import Parser
from Network import Network
from BeautifulSoup import BeautifulSoup

class MangareaderParser(Parser):
    def __init__(self, baseUrl):
        Parser.__init__(self, baseUrl)
        print("Mangareader Parser initialized")

    def getMangaList(self, relativeUrl):
        """ Returns a dictionnary containing the values as key: manga name, value: manga url """
        html = self.network.getUrlContentUtf8(self.baseUrl+relativeUrl)

        self.soup = BeautifulSoup(html)

        # Get all <ul> where there is chapters

        links = {}
        link = self.soup.findAll(lambda tag: tag.name == 'a' and tag.findParent('ul', 'series_alpha'))
        for i in link:
            links[str(i.contents[0]).encode("utf-8")] = str(i['href']).encode("utf-8")
        return links

    def getChapterList(self, relativeUrl):
        """ Returns a dictionnary containing the values as key: chapter title, value: chapter url """
        return {}

    def getChapterImagesUrls(self, relativeUrl):
        """ Returns a dictionnary containing the values as key: image name, value: image url """
        return {}

parser = MangareaderParser("http://www.mangareader.net/")
print(len(parser.getMangaList("alphabetical")))

