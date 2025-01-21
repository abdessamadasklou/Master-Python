import logging
import time
logging.basicConfig(filename='error.log', filemode='w', level=logging.ERROR)
logger = logging.getLogger(__name__)
def log_error(message):
    with open ('error.log', "w") as f:
        f.write(str(time.ctime())+" " + str(message))
    

def read_file(filename):
    try :
        file=open (filename, "r")
        lignes = file.readlines()
        for ligne in lignes:
            print (ligne) 
        
    except FileNotFoundError:
        message="le fichier n'existe pas"
        log_error(message)
        print("le fichier n'existe pas")
    finally:
        if 'file' in locals():
            file.close()

read_file("example.txt")
