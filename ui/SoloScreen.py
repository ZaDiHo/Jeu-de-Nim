from utils.ScreenUtils import *
    
def showSoloScreen():
    from ui.MainScreen import showMainScreen
    from ui.SettingsScreen import showSettingsScreen

    screen = Screen("Jeu de Nim - Mode solo")

    background = Picture(0,0, "./ressources/images/background.png")
    background.resize(1280,720)

    title = Text(823,85,"SOLO",70,)
    menuArea = Area(650,75,550,550)

    def settingsButtonEvent():
        showSettingsScreen()
        pygame.quit()
        
    def startButtonEvent():
        pass

    def backButtonEvent():
        showMainScreen()
        pygame.quit()

    settingsButton = Button(710,190,"Parametres",settingsButtonEvent,425,105)
    startButton = Button(710,325,"Lancer !",startButtonEvent,425,105)
    backButton = Button(710,460,"Retour",backButtonEvent,425,105)

    
    screen.add_element(background)
    screen.add_element(menuArea)
    screen.add_element(settingsButton)
    screen.add_element(startButton)
    screen.add_element(backButton)
    screen.add_element(title)
    
    screen.run()

