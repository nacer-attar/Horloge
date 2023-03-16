import datetime  # Importation du module datetime
import time

Username = input ("Username : ")
print (f" {Username} in the flesh ! 	You’ve proved yourself a decisive man, so I don’t expect you’ll have any trouble deciding what to do. If you’re interested, just step into the portal and I will take that as a yes.")
if 

heure_actuelle = datetime.datetime.now().strftime("%H:%M:%S")
# Obtenir l'heure actuelle sous forme d'objet datetime
# Formatage de l'heure sans les millisecondes
print(heure_actuelle) # Affichage de l'heure formatée


def afficher_heure():
    while True:
        heure_actuelle = datetime.datetime.now().strftime("%H:%M:%S")
        print(heure_actuelle) 
        time.sleep(1)

afficher_heure()
