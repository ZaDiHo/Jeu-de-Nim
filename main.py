from common.NimGame import initValues
from utils.ScreenUtils import Screen
initValues()

screen = Screen("Jeu de Nim")

def startGame():
    from ui.MainScreen import showMainScreen
    showMainScreen(screen)
    
startGame()