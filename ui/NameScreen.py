# Nom du fichier: NameScreen.py
# Auteur: Thomas PROVOST
# Objectif: Ecran du choix du pseudo
# Date dernière modification: 25/01/2021
# Version: 1.0

from utils.ScreenUtils import *

def showNameScreen(screen):
    """
    Affiche l'écran de choix du pseudo
    """
    # Importation de la fonction de manière locale pour éviter les dépendances circulaires
    from common.NimGame import Player
    from client.NimClient import openSession
    from ui.OnlineScreen import showOnlineScreen

    # Nettoyer l'écran
    screen.clear_elements()

    # Ajout du fond de fenêtre
    background = Picture(0, 0, "ressources/images/background.png")
    background.resize(1280,720)

    # Création des éléments
    area = Area(350, 200, 600, 400, "#DED0B6", "#BBAB8C")
    inputArea = Area(400, 350, 500, 125, "#FDF7E4", "#FAEED1")
    inputShadow = Area(415, 450, 450, 5, "#FDF7E4", "#DED0B6")
    
    text = Text(400, 230, "CHOIX PSEUDO", 60)
    pseudo = Text(100, 5, "TEST_PSEU", 60)
    infoText = Text(490, 610, "", 20, (245, 66, 66))

    profil = Picture(10, 10, "./ressources/images/userIcon.png")
    profil.resize(75,75)

    inputBox = InputBox(425, 400, 450, 75, 65, (255,255,255))

    # Définition des événements des boutons
    def handler_click_confirm():
        if(len(inputBox.get_text()) == 0):
            infoText.setText("Veuillez entrer un pseudo !")
            return
        pseudo.setText(inputBox.get_text())
        player = Player(inputBox.get_text())
        client_socket = openSession()
        player.setClientSocket(client_socket)
        showOnlineScreen(screen)
        
    # Création des boutons
    confirmButton = Button(400, 500, "VALIDER", handler_click_confirm, 500, 60, "#FDF7E4", "#FAEED1", 40)

    # Ajout des éléments à l'écran
    screen.add_element(background)
    screen.add_element(area)
    screen.add_element(inputArea)
    screen.add_element(text)
    screen.add_element(pseudo)
    screen.add_element(inputBox)
    screen.add_element(inputShadow)
    screen.add_element(profil)
    screen.add_element(confirmButton)
    screen.add_element(infoText)

    # Boucle principale
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Si l'utilisateur ferme la fenêtre
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN: # Si l'utilisateur clique
                inputBox.handle_event(event)
                if confirmButton.isMouseOver():
                    confirmButton.handle_click()
            elif event.type == pygame.KEYDOWN: # Si l'utilisateur tape
                inputBox.handle_event(event)

        # Dessiner les éléments
        screen.screen.fill((255, 255, 255))
        for element in screen.elements:
            element.draw(screen.screen)

        pygame.display.flip()
        screen.clock.tick(60)

    pygame.quit()