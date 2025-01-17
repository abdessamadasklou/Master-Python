import csv
import os

fichier_contacts = "contacts.csv"

if not os.path.exists(fichier_contacts):
    with open(fichier_contacts, "w", newline="") as fichier:
        writer = csv.writer(fichier)
        writer.writerow(["Nom", "tel", "Ville"])

def ajouter_contact():
    nom = input("Entrez le nom : ")
    tel = input("Entrez le num de tel : ")
    ville = input("Entrez la ville : ")
    with open(fichier_contacts, "a", newline="") as fichier:
        writer = csv.writer(fichier)
        writer.writerow([nom, tel, ville])
    print(f"Contact {nom} ajouté avec succès !")


def afficher_contact():
    try:
        with open(fichier_contacts,"r") as fichier:
            reader = csv.reader(fichier)
            next(reader)
            for ligne in reader:
                if len(ligne) >= 3:
                    print(f"Nom: {ligne[0]}, Tel: {ligne[1]}, ville: {ligne[2]}")

    except FileNotFoundError:
        print("Erreur : Le fichier des contacts n'existe pas.")

def rechercher_contact():
    nom_recherche = input("Entrez le nom à rechercher : ").lower()
    try:
        with open(fichier_contacts, "r") as fichier:
            reader = csv.reader(fichier)
            trouve = False
            for ligne in reader:
                if ligne[0].lower() == nom_recherche.lower():
                    print(f"Nom: {ligne[0]}, Téléphone: {ligne[1]}, Ville: {ligne[2]}")
                    trouve = True
            if not trouve:
                print("Contact non trouvé.")
    except FileNotFoundError:
        print("Erreur : Le fichier des contacts n'existe pas.")

def supprimer_contact():
    nom_supprimer = input("Entrez le nom du contact à supprimer : ").lower()
    with open(fichier_contacts, "r") as fichier:
        reader = csv.reader(fichier)
        contacts = list(reader)

    nouveaux_contacts = [contacts[0]] 
    supprime = False

    for contact in contacts[1:]:
        if contact[0].lower() != nom_supprimer:
            nouveaux_contacts.append(contact)
        else:
            supprime = True

    if supprime:
        with open(fichier_contacts, "w", newline="", encoding="utf-8") as fichier:
            writer = csv.writer(fichier)
            writer.writerows(nouveaux_contacts)
        print(f"Contact '{nom_supprimer}' supprimé avec succès.")
    else:
        print(f"Aucun contact trouvé avec le nom '{nom_supprimer}'.")

def APP():
    while True:
        print("\n--- Gestion des Contacts ---")
        print("1. Ajouter un contact")
        print("2. Afficher tous les contacts")
        print("3. Rechercher un contact par nom")
        print("4. Supprimer un contact")
        print("5. Quitter")
        choix = input("Entrez votre choix : ")

        if choix == "1":
            ajouter_contact()
        elif choix == "2":
            afficher_contact()
        elif choix == "3":
            rechercher_contact()
        elif choix == "4":
            supprimer_contact()
        elif choix == "5":
            print("Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")
APP()