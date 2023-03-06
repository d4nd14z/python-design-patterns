from file import File

class ImageFile(File):

    def __init__(self, name, extension):                
        self.name = name
        self.extension = extension        
    
    def getContent(self):
        return "Este es un archivo de imagen";