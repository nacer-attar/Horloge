"""
This program talks to the user like Half Life's G-Man 
Consider it a giant easter-egg 
goal : a clock that can run either from an user input, the computer's time or as an alarm clock.
"""

import datetime  # Importation du module datetime
import time
import winsound

def user_time():
        # Transformer l'heure de départ en un nombre de secondes depuis minuit
    heures, minutes, secondes = map(int, heure_depart.split(':'))
    depart_en_secondes = heures * 3600 + minutes * 60 + secondes

        # Afficher l'heure actuelle en continu jusqu'à ce que l'utilisateur interrompe le programme
    while True:

        heures = depart_en_secondes // 3600
        minutes = (depart_en_secondes % 3600) // 60
        secondes = depart_en_secondes % 60
        temps = (heures, minutes, secondes)

            # display actual time
        print("{:02d}:{:02d}:{:02d}".format(*temps), end="\r")
        depart_en_secondes += 1
            # wait a second before displaying next time
        time.sleep(1)
def chrono():
    
    start_time = time.time()
    elapsed_time = 0
    start = input ("Press Enter to start")
    i = 0                                                           #setting an ending to the loop until i find a way to make a way to stop when the user want
    while start == "" and i < 200000 :
        jour, remainder = divmod(int(elapsed_time),86400)           # Day + 1 at each 86400 seconds
        heures, remainder = divmod(int(elapsed_time),3600)          # Hour + 1 at each 3600 seconds
        minutes, seconds = divmod(remainder, 60)                    # Minutes +1 at each 60 seconds
        time_values = (jour, heures, minutes,seconds)               # Saving time as a Tuple
        print("{:02d}:{:02d}:{:02d}:{:02d}".format(*time_values), "Press Ctrl + C to stop ",  end='\r')   # displaying tuple in a dd:hh:mm:ss format
        elapsed_time = time.time() - start_time                     # allows Chrono to start from 00:00:00:00   
        time.sleep(1)                                               # Restart the loop after 1 second (optimal to prevent processor from overheating)
        i += 1          
def minuteur():
    duration = int(input(f"Time ! Dr.{Username} : (duration in minutes) ")) * 60 # convert minutes to seconds
    start_time = time.time()
    remaining_time = duration

    while remaining_time > 0:
        jour, remainder = divmod(int(remaining_time),86400)
        heures, remainder = divmod(int(remaining_time),3600)
        minutes, seconds = divmod(remainder, 60)
        time_values = (jour, heures, minutes, seconds)
        print("{:02d}:{:02d}:{:02d}:{:02d}".format(*time_values))
        remaining_time = duration - (time.time() - start_time)
        time.sleep(1)

    print(f"Time, Dr.{Username}!")
def display_time ():
   while True :
    heure_actuelle = datetime.datetime.now().strftime("%H:%M:%S")
    # Obtenir l'heure actuelle sous forme d'objet datetime
    # Formatage de l'heure sans les millisecondes
    print(heure_actuelle,end='\r') # Affichage de l'heure formatée
    time.sleep (1)
def badending_heure():
    i = 0
    while i < 180 :
        heure_actuelle = datetime.datetime.now().strftime("%H:%M:%S")
        print(heure_actuelle)
        time.sleep(1)
        i += 1
def alarm():
# Demander à l'utilisateur l'heure d'alarme
    alarme = input("Entrez l'heure d'alarme (format HH:MM:SS) : ")
        # Transformer l'heure de départ en un nombre de secondes depuis minuit
    heures, minutes, secondes = map(int, heure_depart.split(':'))
    tarheures, tarminutes , tarseconds = map(int, alarme.split(':'))
    depart_en_secondes = heures * 3600 + minutes * 60 + secondes

        # Afficher l'heure actuelle en continu jusqu'à ce que l'utilisateur interrompe le programme
    while True:

        heures = depart_en_secondes // 3600
        minutes = (depart_en_secondes % 3600) // 60
        secondes = depart_en_secondes % 60
        temps = (heures, minutes, secondes)
        alarme = (tarheures, tarminutes, tarseconds)
        # display actual time
        print("{:02d}:{:02d}:{:02d}".format(*temps), end="\r")
    # Obtenir l'heure actuelle et la comparer à l'heure d'alarme
        if temps >= alarme:
            print("ALARME !")
            winsound.Beep(1000, 2000) # Sonnerie pendant 2 secondes
            return False
        depart_en_secondes += 1
        # wait a second before displaying next time
        time.sleep(1)

Username = input ("Username : ")
heure_depart = input(f"Dr.{Username}, Would you please set up the time ? (hh:mm:ss format) : ")

#choisir qu'elle heure on va utiliser pour le programme 
print (f"{Username} in the flesh ! I don’t expect you’ll have any trouble deciding what to do.")
print ("If you’re interested, just follow the rules and I will take that as a yes.")
print ("Otherwise... well... I can offer you a battle you have no chance of winning")
choice = input ("It's time to choose ('set alarm','chrono','timer' or 'else') : " )

if choice == "set alarm" or choice == "alarm" : alarm()
elif choice == "chrono" : chrono()
elif choice == "timer" : minuteur()
else : 
    print ("Hmm ... too bad it ended like this. At least I can let you choose which time you want to see fly by")
    gmanchoice = input ("Time to choose ! ('yours' or 'mine'): ")
    if gmanchoice == "Mine" or "mine" :
        user_time()    
    else : 
        badending_heure()

