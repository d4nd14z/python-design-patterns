from file import File

class PDFFile(File):

    def __init__(self, name, extension):        
        self.name = name
        self.extension = extension

    def getContent(self):
        return "Este es un archivo PDF";