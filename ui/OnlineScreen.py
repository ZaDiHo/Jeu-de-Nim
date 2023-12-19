from utils.ScreenUtils import *

def handler_button():
    print("Button Clicked")
    
def showOnlineScreen():

    screen = Screen("Jeu de Nim - Mode Multijoueur")
    background = Picture(0,0, "./ressources/images/background.png")
    background.resize(1280,720)
    title = Text(755,85,"ENLIGNE",70,)
    menuArea = Area(650,75,550,550)
    soloBtn = Button(710,190,"CREER",handler_button,425,105)
    localBtn = Button(710,325,"REJOINDRE!",handler_button,425,105)
    enligneBtn = Button(710,460,"RETOUR",handler_button,425,105)

    
    screen.add_element(background)
    screen.add_element(menuArea)
    screen.add_element(soloBtn)
    screen.add_element(localBtn)
    screen.add_element(enligneBtn)
    screen.add_element(title)
    
    screen.run()

