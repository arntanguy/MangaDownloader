#!/usr/bin/python
# -*- coding: utf-8 -*-

from Parser import Parser
from BeautifulSoup import BeautifulSoup
from collections import OrderedDict

class MangareaderParser(Parser):
    def __init__(self, baseUrl):
        Parser.__init__(self, baseUrl)
        print("Mangareader Parser initialized")

    def getMangaList(self, relativeUrl):
        """ Returns a dictionnary containing the values as key: manga name, value: manga url """
        html = self.network.getUrlContentUtf8(self.baseUrl+"/"+relativeUrl)

        self.soup = BeautifulSoup(html)

        # Get all <ul> where there is chapters

        links = {}
        linkHtml = self.soup.findAll(lambda tag: tag.name == 'a' and tag.findParent('ul', 'series_alpha'))
        print (linkHtml)
        for i in linkHtml:
            if(len(i.contents) == 1):
                links[str(i.contents[0]).encode("utf-8")] = str(i['href']).encode("utf-8")
        return links

    def getChapterList(self, relativeUrl):
        """ Returns a dictionnary containing the values as key: chapter title, value: chapter url """
        html = self.network.getUrlContentUtf8(self.baseUrl+relativeUrl)
        self.soup = BeautifulSoup(html)
        # Get the links in a dictionnary, ordered by insertion
        links = OrderedDict()
        linkHtml = self.soup.findAll(lambda tag: tag.name == 'a' and tag.findParents('div', {'id' : 'chapterlist'}))
        for i in linkHtml:
            if(len(i.contents) == 1):
                links[str(i.contents[0]).encode('utf-8')] = str(i['href']).encode("utf-8")
        return links

    def getImagesPages(self, chapterRelativeUrl):
        """ Returns a dictionnary containing the values as key: chapter title, value: chapter url """
        html = self.network.getUrlContentUtf8(self.baseUrl+chapterRelativeUrl)
        self.soup = BeautifulSoup(html)
        # Get the links in a dictionnary, ordered by insertion
        links = OrderedDict()
        linkHtml = self.soup.findAll(lambda tag: tag.name == 'option' and tag.findParents('div', {'id' : 'selectpage'}))
        for i in linkHtml:
            if(len(i.contents) == 1):
                links[str(i.contents[0]).encode('utf-8')] = str(i['value']).encode("utf-8")
        return links
    
    def getImagesUrls(self, relativeUrlList):
        """ Returns a dictionnary containing the values as key: image name, value: image url """
        links = OrderedDict()

        for imagePage in relativeUrlList:
            html = self.network.getUrlContentUtf8(self.baseUrl+imagePage.decode("utf-8"))
            self.soup = BeautifulSoup(html)
            link = self.soup.findAll(lambda tag: tag.name == 'img' and tag.findParents('div', {'id' : 'imgholder'}))
            for i in link:
                links[str(i['alt']).encode("utf-8")] = str(i['src']).encode("utf-8")
        return links

parser = MangareaderParser("http://www.mangareader.net")
#print(len(parser.getMangaList("alphabetical")))
#chapterList = parser.getChapterList("/250/7th-period-is-a-secret.html")
#print(chapterList)
#images = parser.getImagesPages(chapterList[0][1])
#imagePages = parser.getImagesPages("/250-17691-1/7th-period-is-a-secret/chapter-2.html")
#print(imagePages)
#images = parser.getImagesUrls(imagePages.values())
#print(images)


