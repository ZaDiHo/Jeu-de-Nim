# Nom du fichier: OnlineScreen.py
# Auteur: Thomas PROVOST
# Objectif: Ecran du jeu en ligne
# Date dernière modification: 25/01/2021
# Version: 1.0

from utils.ScreenUtils import *
    
def showOnlineScreen(screen):

    # Nettoyage de l'écran
    screen.clear_elements()

    # Ajout du fond de fenêtre
    background = Picture(0,0, "./ressources/images/background.png")
    background.resize(1280,720)

    # Ajout des éléments
    title = Text(755,85,"ENLIGNE",70,)
    menuArea = Area(650,75,550,550)

    # Définition des événements des boutons
    def handler_button():
        return None
    
    # Création des boutons
    soloBtn = Button(710,190,"CREER",handler_button,425,105)
    localBtn = Button(710,325,"REJOINDRE!",handler_button,425,105)
    enligneBtn = Button(710,460,"RETOUR",handler_button,425,105)

    # Ajout des éléments à l'écran
    screen.add_element(background)
    screen.add_element(menuArea)
    screen.add_element(soloBtn)
    screen.add_element(localBtn)
    screen.add_element(enligneBtn)
    screen.add_element(title)
    
    # Lancer la fenêtre
    screen.run()

