
import os
import re
import sys

class Directory:

  def makePretty(name):
    """Returns the chain given, in order to have a normal name"""
    return str(name).capitalize().replace("/", "").replace("_", " ")

    def initialise(self,manga):
        self.manga = manga
        self.mangaPretty = makePretty(manga)
        self.url = "http://mangareader.net/" 
        self.numberImage=0
        # Create the download directory
        try:
            if (os.path.isdir(downloadDirectory) == False):
                os.mkdir(downloadDirectory)
            if (os.path.isdir(downloadDirectory + self.mangaPretty) == False):
                os.mkdir(downloadDirectory + self.mangaPretty)
        except OSError:
            printError("Unable to create the download directory")
            exit(1)
    
    def chapterDirectoryName(self, number):
        """Returns the name of the directory of the chapter.
            It is useful in order to organize the mass of chapters.
            example:
            500 chaps in the manga, directory named "001" instead of "1" """
        number = str(number)
        return (mangaNumberLenght - len(number))*"0"+ number
      
      
    mangaDirectory = downloadDirectory + self.mangaPretty +"/" + self.chapterDirectoryNname(number)
        if (os.path.isdir(mangaDirectory) == False):
            os.mkdir(mangaDirectory)
        os.chdir(mangaDirectory)
        
        self.getImages(images)


