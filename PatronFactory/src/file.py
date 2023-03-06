class File: 

    def __init__(self):        
        self.path = None
        self.name = None
        self.extension = None

    def getPath(self):
        return self.path

    def getName(self):
        return self.name

    def getExtension(self):
        return self.extension

    def __str__(self):
        return f"Name: {self.getName()} Extension: {self.getExtension()}"