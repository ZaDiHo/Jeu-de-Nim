import random

from utils.ScreenUtils import *

def showLoadingScreen(screen):
    from ui.SoloSettingsScreen import Screen


    screen.clear_elements()
    background = Picture(0,0, "./ressources/images/background.png")
    background.resize(1280,720)

    title = ["DEMARRAGE.", "DEMARRAGE..", "DEMARRAGE..."]
    tips =  ["Text 1", "Text 2", "Text 3", "Text 4", "Text 5", "Text 6", "Text 7", "Text 8", "Text 9", "Text 10"]



    upperArea = Area(280, 100, 750, 100)
    bottomArea = Area(280, 300, 750, 250)



    screen.add_element(background)
    screen.add_element(upperArea)
    screen.add_element(bottomArea)

    screen.run()