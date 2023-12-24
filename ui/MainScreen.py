from utils.ScreenUtils import *

def showMainScreen(screen):
    from ui.NameScreen import showNameScreen
    from ui.SoloScreen import showSoloScreen
    from ui.LocalScreen import showLocalScreen
    screen.clear_elements()
    
    background = Picture(0,0, "./ressources/images/background.png")
    background.resize(1280,720)
    credit = Text(10,700,"Projet NSI 2023 réalisé par Adame et Thomas",10)
    title = Text(390,85,"JEU DE NIM",70,)

    menuArea = Area(350,75,550,550)

    def soloButtonEvent():
        showSoloScreen(screen)
        
    def localButtonEvent():
        showLocalScreen(screen)

    def onlineButtonEvent():
        showNameScreen(screen)

    soloButton = Button(410,190,"Solo",soloButtonEvent,425,105)
    localButton = Button(410,325,"Local",localButtonEvent,425,105)
    onlineButton = Button(410,460,"En ligne",onlineButtonEvent,425,105)

    
    screen.add_element(background)
    screen.add_element(credit)
    screen.add_element(menuArea)
    screen.add_element(soloButton)
    screen.add_element(localButton)
    screen.add_element(onlineButton)
    screen.add_element(title)

    screen.run()