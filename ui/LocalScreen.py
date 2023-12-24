from utils.ScreenUtils import *
    
def showLocalScreen(screen):
    from ui.MainScreen import showMainScreen
    from ui.LocalSettingsScreen import showLocalSettingsScreen

    screen.clear_elements()

    background = Picture(0,0, "./ressources/images/background.png")
    background.resize(1280,720)

    title = Text(823,85,"LOCAL",70,)
    vsText = Text(250, 295, "CONTRE", 40)
    firstPlayerText = Text(190, 250, "1. PLAYER_12345", 30)
    secondPlayerText = Text(190, 370, "2. PLAYER_67891", 30)
    menuArea = Area(650,75,550,550)

    nameArea = Area(100, 205, 500, 250)

    def settingsButtonEvent():
        showLocalSettingsScreen(screen)
        
    def startButtonEvent():
        pass

    def backButtonEvent():
        showMainScreen(screen)

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
    screen.add_element(vsText)
    screen.add_element(firstPlayerText)
    screen.add_element(secondPlayerText)
    
    screen.run()

