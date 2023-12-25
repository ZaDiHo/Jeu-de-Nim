# Nom du fichier: GameUtils.py
# Auteur: Thomas PROVOST
# Objectif: Utilitaire pour la gestion des parties en ligne
# Date dernière modification: 25/01/2021
# Version: 1.0

import random

def generateId(number):
    """
    Génère un identifiant aléatoire de la longueur spécifiée
    
    Paramètres:
    * number: longueur de l'identifiant
    """
    id_list = [random.randint(0, 9) for _ in range(number)]
    return id_list

def verifyDuplicateId(firstId, secondId):
    """
    Vérifie si deux identifiants sont identiques sinon en génère un nouveau
    
    Paramètres:
    * firstId: premier identifiant
    * secondId: deuxième identifiant
    """
    if(firstId == secondId):
        while firstId == secondId:
            secondId = generateId(5)
        return secondId
    else:
        return secondId