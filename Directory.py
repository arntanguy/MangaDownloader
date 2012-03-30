
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
    os.listdir(mangaDirectory)
    return max(float(os.listdir(mangaDirectory))
		
		
  def chapterMissing(mangaDirectory):
    """Search if chapter are missing"""
    i=0
    while i < len(os.listdir(mangaDirectory)):
        if int(((os.listdir(mangaDirectory))[i]) != i+1:
          print "chapter," (os.listdir(mangaDirectory))[i])+1 "to" (listdir(mangadrectory))[i+1] "are missing"
          i=i+1
          return range((os.listdir(donwlaodDirectory))[i]+1,(os.listdir(donwlaodDirectory))[i+1]
	  exit(2)
	else:
          i=i+1 		
				
  def mangaDownloaded(mangaDirectory):
    """search if the manga directory exist"""
    for i in os.listdir(donwlaodDirectory):
      if (os.listdir(donwlaodDirectory))[i]== mangaDirectory
        print("the manga exist in the directory")
        return le_lapin_est_dans_le_chapeau 
        exit(3)
      elif i==len(os.listdir(donwlaodDirectory)):
        print("the manga does not exist in the directory")
        return le_lapin_n_est_pas_dans_le_chapeau
        
