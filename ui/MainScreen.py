# Nom du fichier: MainScreen.py
# Auteur(s): Abdelrahman AL KHATIB, Thomas PROVOST
# Objectif: Ecran d'accueil
# Date dernière modification: 25/01/2021
# Version: 1.3

from utils.ScreenUtils import *

def showMainScreen(screen):
    """
    Affiche l'écran principal
    """
    # Importation de la fonction de manière locale pour éviter les dépendances circulaires
    from ui.SoloScreen import showSoloScreen
    from ui.LocalScreen import showLocalScreen
    from common.NimGame import setMode

    # Nettoyer l'écran
    screen.clear_elements()
    
    # Ajout du fond de fenêtre
    background = Picture(0,0, "./ressources/images/background.png")
    background.resize(1280,720)

    # Création des éléments
    credit = Text(315,680,"Projet NSI 2023 réalisé par Abdelrahman et Thomas",20)
    title = Text(390,85,"JEU DE NIM",70,)

    menuArea = Area(350,75,550,550)

    # Définition des événements des boutons
    def soloButtonEvent():
        """
        Affiche l'écran de jeu solo
        """
        setMode(1)
        showSoloScreen(screen)
        
    def localButtonEvent():
        """
        Affiche l'écran de jeu local
        """
        setMode(2)
        showLocalScreen(screen)

    def quitButtonEvent():
        """
        Affiche l'écran de jeu en ligne
        """
        exit()

    # Création des boutons
    soloButton = Button(410,190,"Solo",soloButtonEvent,425,105)
    localButton = Button(410,325,"Local",localButtonEvent,425,105)
    quitButton = Button(410,460,"Quitter",quitButtonEvent,425,105)

    # Ajout des éléments à l'écran
    screen.add_element(background)
    screen.add_element(credit)
    screen.add_element(menuArea)
    screen.add_element(soloButton)
    screen.add_element(localButton)
    screen.add_element(quitButton)
    screen.add_element(title)

    # Lancer la fenêtre
    screen.run()