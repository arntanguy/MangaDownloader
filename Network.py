import urllib.request


class Network:
    def __init__(self):
        # note that Python3 does not read the html code as string
        # but as html code bytearray, convert to string with

    def getUrlContent(url):
        """ Returns an html code bytearray containing the content of the downloaded page.
        This is a synchrone method """
        url = urllib.request.urlopen(url)
        bytes = url.read()
        return bytes

    def getUrlContentUtf8(url):
        htmlByteArray = getUrlContent(url)
        return htmlByteArray.decode("utf8")

network = Network()

