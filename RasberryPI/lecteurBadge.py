#!/usr/bin/env python3.7
# -- coding: utf-8 --

import RPi.GPIO as GPIO  # Importe la bibliothèque pour contrôler les GPIOs
from pirc522 import RFID
import time


GPIO.setmode(GPIO.BOARD)  # Définit le mode de numérotation (Board)
GPIO.setwarnings(False)  # On désactive les messages d'alerte

rc522 = RFID()  # On instancie la lib

# On affiche un message demandant à l'utilisateur de passer son badge
print('En attente d\'un badge (pour quitter, Ctrl + c): ')

# On va faire une boucle infinie pour lire en boucle
while True:
    rc522.wait_for_tag()  # On attnd qu'une puce RFID passe à portée
    # Quand une puce a été lue, on récupère ses infos
    (error, tag_type) = rc522.request()

    if not error:  # Si on a pas d'erreur
        # On nettoie les possibles collisions, ça arrive si plusieurs cartes passent en même temps
        (error, uid) = rc522.anticoll()

        if not error:  # Si on a réussi à nettoyer
            # On affiche l'identifiant unique du badge RFID
            print('Vous avez passé le badge avec l\'id : {}'.format(uid))
            # On attend 1 seconde pour ne pas lire le tag des centaines de fois en quelques milli-secondes
            time.sleep(1)