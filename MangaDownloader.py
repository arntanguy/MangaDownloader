'''
Created on Mar 31, 2012

@author: arnaud
'''

from MangareaderParser import MangareaderParser
from Network import Network
from Console import Console
import argparse
import os

class MangaDownloader:
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.siteUrl = "http://www.mangareader.net"
        self.mangalistRelativeUrl = "/alphabetical"
        self.parser = MangareaderParser(self.siteUrl)
        self.network = Network()
        self.console = Console()
        
        self.consoleParse = argparse.ArgumentParser(description='Process some integers.')
        self.consoleParse.add_argument('integers', metavar='N', type=int, nargs='+',
                   help='an integer for the accumulator')
        self.consoleParser.add_argument('--sum', dest='accumulate', action='store_const',
                   const=sum, default=max,
                   help='sum the integers (default: find the max)')

  
    def setParser(self, parser):
        self.parser = parser
    
    def showMangaList(self):
        self.parser.getMangaList(self.mangalistRelativeUrl)
    
    def downloadChapter(self, chapterRealativeUrl):
        imgPages = self.parser.getImagesPages(chapterRealativeUrl)
        print(imgPages)
        imagesUrls = self.parser.getImagesUrls(imgPages.values())
        print(imagesUrls)
        i=0
        for imageUrl in imagesUrls.values():
            print("Downloading "+str(imageUrl))
            self.network.downloadFile(str(imageUrl, "utf-8"), str(i))
            i+=1
            
mangaDownloader = MangaDownloader()
mangaDownloader.downloadChapter("/250-17691-1/7th-period-is-a-secret/chapter-2.html")
            
        
        