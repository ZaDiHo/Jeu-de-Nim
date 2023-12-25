# Nom du fichier: main.py
# Auteur: Abdelrahman AL KHATIB
# Objectif: Fichier principal du jeu
# Date dernière modification: 25/01/2021
# Version: 1.1

# Importation des modules
from common.NimGame import initValues
from utils.ScreenUtils import Screen

# Initialisation des valeurs
initValues()

# Création de l'écran de l'application
screen = Screen("Jeu de Nim")

# Définition de la fonction de démarrage du jeu
def startGame():
    """
    Démarre le jeu
    """
    # Importation de la fonction de manière locale pour éviter les dépendances circulaires
    from ui.MainScreen import showMainScreen

    # Affichage de l'écran principal
    showMainScreen(screen)
    
# Démarrage du jeu
startGame()