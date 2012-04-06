
import os
from Console import Console

class Directory:
    def __init__(self, manga):
        self.downloadDirectory = "/media/DATA/Linux/personnel/Mangas"
        self.manga = manga
        self.mangaPretty = self.makePretty(manga)
        self.numberImage = 0
        self.console = Console()   
        
    def createDownloadDirectory(self, manga):
        # Create the download directory
        try:
            if (os.path.isdir(self.downloadDirectory) == False):
                os.mkdir(self.downloadDirectory)
            if (os.path.isdir(self.downloadDirectory + self.mangaPretty) == False):
                os.mkdir(self.downloadDirectory + self.mangaPretty)
        except OSError:
            self.console.printError("Unable to create the download directory")
            exit(1)
   
    def makePretty(self, name):
        """Returns the chain given, in order to have a normal name"""
        return str(name).capitalize().replace("/", "").replace("_", " ")

    def chapterDirectoryName(self, number):
        """Returns the name of the directory of the chapter.
           It is useful in order to organize the mass of chapters.
           example:
           500 chaps in the manga,��directory named "001" instead of "1" """
        number = str(number)
        return (mangaNumberLenght - len(number)) * "0" + number


        mangaDirectory = downloadDirectory + self.mangaPretty + "/" + self.chapterDirectoryNname(number)
        if (os.path.isdir(mangaDirectory) == False):
            os.mkdir(mangaDirectory)
        os.chdir(mangaDirectory)



    def lastChapter(self, mangaDirectory):
        """Return the last chapter directory of the manga"""
        return max(float(os.listdir(mangaDirectory)))

    def chapterMissing(self, mangaDirectory):
      """ Returns a list of local missing chapters """
      missing = []
      i = 1
      for chapter in os.listdir(mangaDirectory):
          if chapter != i or len(os.listdir(chapter)) == 0:
              missing = range(i, chapter) + missing
              i = chapter
          i += 1
      return missing



    def mangaDownloaded(self, mangaDirectory):
      """search if the manga directory exist"""
      for manga in os.listdir(downloadDirectory):
          if manga == mangaDirectory:
              return True
      print("The Manga does not exist in the directory!")
      return False
