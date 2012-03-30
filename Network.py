import urllib.request


class Network:
    def __init__(self):
        # note that Python3 does not read the html code as string
        # but as html code bytearray, convert to string with
        print("Initialize Network")

    def getUrlContent(self, url):
        """ Returns an html code bytearray containing the content of the downloaded page.
        This is a synchrone method """
        url = urllib.request.urlopen(url)
        bytes = url.read()
        return bytes

    def getUrlContentUtf8(self, url):
        htmlByteArray = self.getUrlContent(url)
        return htmlByteArray.decode("utf8")

network = Network()

