import csv

# Données à écrire dans le fichier CSV
donnees = [
    ["Nom", "Age", "Ville"],["Yassine", 30, "azrou"]
]

with open("contacts.csv", "w", newline='') as fichier:
    ss = csv.writer(fichier)
    ss.writerows(donnees)
with open("contacts.csv", "r", newline='') as fichier:
    ss = csv.reader(fichier)
    next (ss)
    for ligne in ss:
        print(f"Nom: {ligne[0]} - Age: {ligne[1]} - Ville: {ligne[2]}")