import shutil
import os

with open ("journal.txt","w") as fichier :
    lignes=[" ligne 1\n", " ligne 2\n", " ligne 3\n", " ligne 4\n"]
    fichier.writelines(lignes)

source="journal.txt"
desti="journal_copie.txt"

try :
    shutil.copy(source, desti)
    print(f"fichier copie de {source} a {desti}.")
except FileNotFoundError:
    print(f"Le fichier {source} n'existe pas.")
except Exception as e:
    print(f"Erreur lors de la copie : {e}")

source1="journal_copie.txt"
desti1="archives/journal_copie.txt"

try:
   if not os.path.exists("archives"):
        os.makedirs("archives")
        print("Dossier 'archives' créé avec succès.")

        shutil.move(source1,desti1)
        print(f"fichier deplace de {source} a {desti1}")
except FileNotFoundError:
    print(f"Le fichier a deplacer n'existe pas.")
except Exception as e:
    print(f"Erreur lors de deplacement: {e}")
