from utils.ScreenUtils import *
    
def showSoloScreen(screen):
    from ui.MainScreen import showMainScreen
    from ui.SoloSettingsScreen import showSoloSettingsScreen
    from ui.MatchScreen import showMatchScreen
    screen.clear_elements()

    background = Picture(0,0, "./ressources/images/background.png")
    background.resize(1280,720)

    title = Text(530,85,"SOLO",70,)
    menuArea = Area(350,75,550,550)

    def settingsButtonEvent():
        showSoloSettingsScreen(screen)
        
    def startButtonEvent():
        showMatchScreen(screen)

    def backButtonEvent():
        showMainScreen(screen)

    settingsButton = Button(410,190,"Parametres",settingsButtonEvent,425,105)
    startButton = Button(410,325,"Lancer !",startButtonEvent,425,105)
    backButton = Button(410,460,"Retour",backButtonEvent,425,105)

    
    screen.add_element(background)
    screen.add_element(menuArea)
    screen.add_element(settingsButton)
    screen.add_element(startButton)
    screen.add_element(backButton)
    screen.add_element(title)
    
    screen.run()

