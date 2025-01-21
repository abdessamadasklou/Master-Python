def read_file(filename):
    try :
        file=open (filename, "r")
        lignes = file.readlines()
        for ligne in lignes:
            print (ligne) 
        
    except FileNotFoundError:
        print("le fichier n'existe pas")
    finally:
        if 'file' in locals():
            file.close()
if __name__=="__main__":
    read_file("ex1.py")