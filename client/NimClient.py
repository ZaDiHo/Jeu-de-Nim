# Nom du fichier: NimClient.py
# Auteur: Thomas PROVOST
# Objectif: Client du jeu Nim
# Date dernière modification: 25/01/2021
# Version: 1.3

import socket
import threading
import os
from dotenv import load_dotenv

# Définition des fonctions
def getAnswers(socket):
    """
    Fonction qui reçoit les réponses du serveur en arrière-plan

    Paramètres :
    * socket : le socket client
    """
    # Boucle infinie pour recevoir les réponses du serveur
    while True:
        try:
            reponse = socket.recv(1024).decode('utf-8')
            print(reponse)
        except Exception as e:
            print(f"Erreur lors de la réception de la réponse : {e}")
            break

def sendCommand(socket, commande):
    """
    Envoie une commande au serveur

    Paramètres :
    * socket : le socket client
    * commande : la commande à envoyer au serveur
    """
    socket.send(commande.encode('utf-8'))

def openSession():
    """
    Ouvre une session avec le serveur.
    """
    # Récupération de l'adresse IP du serveur
    load_dotenv()
    server_ip = os.getenv("SERVER_IP")

    # Connexion au serveur
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, 5555))

    # Lancement du thread pour recevoir les réponses du serveur en arrière-plan
    thread_reception = threading.Thread(target=getAnswers, args=(client_socket,))
    thread_reception.start()

    # Retourne le socket client
    return client_socket