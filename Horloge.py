import datetime  # Importation du module datetime
import time

Username = input ("Username : ")


def chrono():
    duration = int(input(f"Time ! Dr.{Username} : (duration in second) "))
    start_time = time.time()
    elapsed_time = 0

    while elapsed_time < duration :
        jour, remainder = divmod(int(elapsed_time),86400)
        heures, remainder = divmod(int(elapsed_time),3600)
        minutes, seconds = divmod(remainder, 60)
        time_values = (jour, heures, minutes, seconds)
        print("{:02d}:{:02d}:{:02d}:{:02d}".format(*time_values))
        elapsed_time = time.time() - start_time
        time.sleep(0.01)


chrono()
"""

quelle_heure = print ("Which time you want to display ? Yours or Mine ? ")
print (f" {Username} in the flesh ! I don’t expect you’ll have any trouble deciding what to do.")
print ("If you’re interested, just type 'set alarm' and I will take that as a yes.")
print ("Otherwise... well... I can offer you to witness the time passing")
choice = input ("It's time to choose ('set alarm' or 'else') : " )

def display_time ():
    heure_actuelle = datetime.datetime.now().strftime("%H:%M:%S")
    # Obtenir l'heure actuelle sous forme d'objet datetime
    # Formatage de l'heure sans les millisecondes
    print(heure_actuelle) # Affichage de l'heure formatée

def badending_heure():
    i = 0
    while i < 180 :
        heure_actuelle = datetime.datetime.now().strftime("%H:%M:%S")
        print(heure_actuelle) 
        time.sleep(1)
        i += 1


if choice == "set alarm" : ()

else :
    badending_heure()




def user_time():
    # Demander à l'utilisateur l'heure de départ
    heure_depart = input("Entrez l'heure de départ au format hh:mm:ss : ")

    # Transformer l'heure de départ en un nombre de secondes depuis minuit
    heures, minutes, secondes = map(int, heure_depart.split(':'))
    depart_en_secondes = heures * 3600 + minutes * 60 + secondes

    # Afficher l'heure actuelle en continu jusqu'à ce que l'utilisateur interrompe le programme
    while True:
        # Obtenir l'heure actuelle en secondes depuis minuit
        maintenant_en_secondes = time.time() % 86400

        # Calculer le temps écoulé depuis l'heure de départ
        temps_ecoule = maintenant_en_secondes - depart_en_secondes
        if temps_ecoule < 0:
            temps_ecoule += 86400

        # Convertir le temps écoulé en heures, minutes et secondes
        heures = temps_ecoule // 3600
        minutes = (temps_ecoule % 3600) // 60
        secondes = temps_ecoule % 60

        # Afficher l'heure actuelle
        print("{:02d}:{:02d}:{:02d}".format(heures, minutes, secondes))

        # Attendre une seconde avant d'afficher l'heure suivante
        time.sleep(1)
"""