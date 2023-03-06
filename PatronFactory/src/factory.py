import os
from entities.image import ImageFile
from entities.text import TextFile
from entities.pdf import PDFFile

class Factory:

    def createFile(self, filename):         
        name, extension = os.path.splitext(filename)
        if extension in [".jpg", ".jpeg", ".png"]: 
            return ImageFile(name, extension)
        elif extension in [".txt", ".md"]: 
            return TextFile(name, extension)
        elif extension in [".pdf"]:
            return PDFFile(name, extension)