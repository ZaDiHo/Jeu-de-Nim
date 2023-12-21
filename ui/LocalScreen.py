from utils.ScreenUtils import *
    
def showLocalScreen():
    from ui.MainScreen import showMainScreen
    from ui.LocalSettingsScreen import showLocalSettingsScreen

    screen = Screen("Jeu de Nim - Mode local")

    background = Picture(0,0, "./ressources/images/background.png")
    background.resize(1280,720)

    title = Text(823,85,"LOCAL",70,)
    menuArea = Area(650,75,550,550)

    nameArea = Area(350, 75, 550, 300)

    def settingsButtonEvent():
        showLocalSettingsScreen()
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
    screen.add_element(nameArea)
    
    screen.run()

