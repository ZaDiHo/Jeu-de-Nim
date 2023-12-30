# Nom du fichier: SoloScreen.py
# Auteur(s): Abdelrahman AL KHATIB
# Objectif: Ecran du jeu solo
# Date dernière modification: 25/01/2021
# Version: 1.5
# Code Reviewer: Thomas PROVOST

from utils.ScreenUtils import *
    
def showSoloScreen(screen):
    """
    Affiche l'écran de jeu solo
    """
    # Importation de la fonction de manière locale pour éviter les dépendances circulaires
    from ui.MainScreen import showMainScreen
    from ui.SoloSettingsScreen import showSoloSettingsScreen
    from ui.MatchScreen import showMatchScreen

    # Nettoyer l'écran
    screen.clear_elements()

    # Ajout du fond de fenêtre
    background = Picture(0,0, "./ressources/images/background.png")
    background.resize(1280,720)

    # Création des éléments
    title = Text(530,85,"SOLO",70,)
    menuArea = Area(350,75,550,550)

    # Définition des événements des boutons
    def settingsButtonEvent():
        """
        Affiche l'écran des paramètres du mode solo
        """
        showSoloSettingsScreen(screen)
        
    def startButtonEvent():
        """
        Démarre le jeu
        """
        showMatchScreen(screen)

    def backButtonEvent():
        """
        Retourne à l'écran principal
        """
        showMainScreen(screen)

    # Création des boutons
    settingsButton = Button(410,190,"Parametres",settingsButtonEvent,425,105)
    startButton = Button(410,325,"Lancer !",startButtonEvent,425,105)
    backButton = Button(410,460,"Retour",backButtonEvent,425,105)

    # Ajout des éléments à l'écran
    screen.add_element(background)
    screen.add_element(menuArea)
    screen.add_element(settingsButton)
    screen.add_element(startButton)
    screen.add_element(backButton)
    screen.add_element(title)
    
    # Lancer la fenêtre
    screen.run()

