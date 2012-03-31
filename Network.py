import socket
import urllib.request
from Console import Console

#import urllib error handling
from urllib.error import HTTPError, URLError

           

class Network:
    def __init__(self):
        # note that Python3 does not read the html code as string
        # but as html code bytearray, convert to string with
        self.maxTries = 5
        self.console = Console()
        print("Initialize Network")

    def getUrlContentUtf8(self, url):
        htmlByteArray = self.getUrlContent(url)
        return htmlByteArray.decode("utf8")

    def getUrlContent(self, url):
        """Returns the content of a webpage at the given url"""
        self.console.printNormal("Donwloading " + url)
        tries = 0
        downloaded = False
        while tries < self.maxTries and downloaded == False:
            try:
                ret = urllib.request.urlopen(url)
                downloaded = True
            except(IOError, socket.error):
                tries += 1
                if tries == self.maxTries:
                    self.console.printError("Maximum tries number reached exiting...")
                    exit(1)
                else:
                    self.console.printError("Failed download, retrying...")
                self.console.printError("Failed download, retrying...")
        self.console.printSuccess("Downloaded!")
        return ret.read()

    def downloadFile(self, url, localName):
        """Retrieves a file"""
        tries = 0
        downloaded = False
        while tries < self.maxTries and downloaded == False:
            try:
                urllib.request.urlretrieve(url, localName)
                downloaded = True
            except HTTPError as e:
                self.console.printError("HTTP Error:", e.code , url)
                tries += 1
            except URLError as e:
                self.console.printError("URL Error:", e.reason , url)
                tries += 1
            if(tries == self.maxTries):
                self.console.printError("Maximum tries number reached exiting...")
                exit(1)
                  
            self.console.printSuccess(url + " downloaded to " + localName)

#net = Network()
#net.downloadFile(http://i13.mangareader.net/7th-period-is-a-secret/2/7th-period-is-a-secret-402446.jpg"), "test.jpg")