import os
import factory
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    sourcePath = os.getenv("DOCUMENT_FOLDER")
    myFactory = factory.Factory()    
    if os.path.isdir(sourcePath): 
        for filename in os.listdir(sourcePath):            
            archivo = myFactory.createFile(filename)
            print(archivo.getContent())
        del myFactory # Destroy object 
    else:        
        raise Exception("ERROR: El directorio de procesamiento no existe o no es una ruta valida.")
        
    