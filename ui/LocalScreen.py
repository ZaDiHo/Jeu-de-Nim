# Nom du fichier: LocalScreen.py
# Auteur: Abdelrahman AL KHATIB
# Objectif: Ecran du jeu local
# Date dernière modification: 25/01/2021
# Version: 1.1
# Code Reviewer: Thomas PROVOST

from utils.ScreenUtils import *
    
def showLocalScreen(screen):
    """
    Affiche l'écran de jeu local

    Paramètres:
    * screen: l'écran sur lequel afficher les éléments
    """
    # Import des fonctions de manière locale pour éviter les dépendances circulaires
    from ui.MainScreen import showMainScreen
    from ui.MatchScreen import showMatchScreen
    from ui.LocalSettingsScreen import showLocalSettingsScreen
    from common.NimGame import getFirstPlayerName, getSecondPlayerName, setFirstPlayerName, setSecondPlayerName

    # Nettoyer l'écran
    screen.clear_elements()

    # Ajout du fond de fenêtre
    background = Picture(0,0, "./ressources/images/background.png")
    background.resize(1280,720)

    # Création des éléments
    title = Text(810,85,"LOCAL",70,)
    vsText = Text(250, 295, "CONTRE", 40)

    firstPlayerName = InputBox(230, 255, 300, 40, 40, (255,255,255), "#DED0B6")
    secondPlayerName = InputBox(230, 375, 300, 40, 40, (255,255,255), "#DED0B6")
    firstPlayerName.text = getFirstPlayerName()
    secondPlayerName.text = getSecondPlayerName()

    firstPlayerText = Text(190, 250, "1. _________________", 30)
    secondPlayerText = Text(190, 370, "2. _________________", 30)

    menuArea = Area(650,75,550,550)
    nameArea = Area(100, 205, 500, 250)

    # Définition des événements des boutons
    def settingsButtonEvent():
        """
        Affiche l'écran des paramètres du jeu local
        """
        setFirstPlayerName(firstPlayerName.text)
        setSecondPlayerName(secondPlayerName.text)
        showLocalSettingsScreen(screen)
        
    def startButtonEvent():
        """
        Démarre le jeu
        """
        setFirstPlayerName(firstPlayerName.text)
        setSecondPlayerName(secondPlayerName.text)
        showMatchScreen(screen)

    def backButtonEvent():
        """
        Retourne à l'écran principal
        """
        showMainScreen(screen)

    # Création des boutons
    settingsButton = Button(710,190,"Parametres",settingsButtonEvent,425,105)
    startButton = Button(710,325,"Lancer !",startButtonEvent,425,105)
    backButton = Button(710,460,"Retour",backButtonEvent,425,105)

    # Ajout des éléments à l'écran
    screen.add_element(background)
    screen.add_element(menuArea)
    screen.add_element(settingsButton)
    screen.add_element(startButton)
    screen.add_element(backButton)
    screen.add_element(title)
    screen.add_element(nameArea)
    screen.add_element(vsText)
    screen.add_element(firstPlayerText)
    screen.add_element(secondPlayerText)
    screen.add_element(firstPlayerName)
    screen.add_element(secondPlayerName)

    # Boucle principale
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Si l'utilisateur ferme la fenêtre
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN: # Si l'utilisateur clique
                firstPlayerName.handle_event(event)
                secondPlayerName.handle_event(event)
                if settingsButton.isMouseOver():
                    settingsButton.handle_click()
                elif startButton.isMouseOver():
                    startButton.handle_click()
                elif backButton.isMouseOver():
                    backButton.handle_click()
            elif event.type == pygame.KEYDOWN: # Si l'utilisateur tape
                firstPlayerName.handle_event(event)
                secondPlayerName.handle_event(event)

        # Dessiner les éléments
        screen.screen.fill((255, 255, 255))
        for element in screen.elements:
            element.draw(screen.screen)

        pygame.display.flip()
        screen.clock.tick(60)

    # Lancer la fenêtre
    screen.run()