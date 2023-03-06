import os
from file import File

class TextFile(File):

    def __init__(self, name, extension): 
        self.path = os.getenv("DOCUMENT_FOLDER")       
        self.name = name
        self.extension = extension

    def getContent(self):         
        text = ""
        try:                         
            filePath = self.path + '/' + self.name + self.extension
            f = open (filePath, 'r')    
            text = f.read() 
            f.close()                                             
        except Exception as ex:
            text = str(ex)
            raise(ex)
        finally: 
            return text