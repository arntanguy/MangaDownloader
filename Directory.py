
import os
import re
import sys


class Directory:
  def makePretty(name):
    """Returns the chain given, in order to have a normal name"""
    return str(name).capitalize().replace("/", "").replace("_", " ")

  def initialize(self,manga):
    self.manga = manga
    self.mangaPretty = makePretty(manga)
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



  def lastChapter(mangaDirectory):
    """Return the last chapter directory of the manga"""
    return max(float(os.listdir(mangaDirectory))

  def chapterMissing(mangaDirectory):
    """ Returns a list of local missing chapters """
    missing=[]
    i = 1
    for chapter in os.listdir(mangaDirectory):
        if chapter != i or len(os.listdir(chapter)) == 0:
            missing = range(i, chapter) + missing
            i = chapter
        i+=1
    return missing
	
	
  
  
  def mangaDownloaded(mangaDirectory):
    """search if the manga directory exist"""
    for manga in os.listdir(downloadDirectory):
        if manga == mangaDirectory:
            return True
    print("The Manga does not exist in the directory!")
    return False
    
  
