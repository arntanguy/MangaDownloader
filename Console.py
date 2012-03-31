'''
Created on Mar 31, 2012

@author: arnaud
'''

class Console(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    def printNormal(self, text):
        print(text)
        
    def printError(self, text):
        print('\033[31;1m%s\033[0m', text)

    def printSuccess(self, text):
        print("\033[32;40m%s\033[0m", text)

        