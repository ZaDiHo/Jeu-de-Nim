from utils.ScreenUtils import *

def showMatchScreen():
    from ui.SoloScreen import showSoloScreen
    from ui.SoloSettingsScreen import showSoloSettingsScreen
    from common.NimGame import getMaxNumberOfMatchesTakeable
    from common.NimGame import setMaxNumberOfMatchesTakeable
    from common.NimGame import getMatches
    from common.NimGame import setMatches
    from ui.MainScreen import showMainScreen
    from ui.LoadingScreen import showLoadingScreen

    def nullEvent():
        return None


    def backButtonEvent():
        showMainScreen()
        pygame.quit()

    def validateButtonEvent():
        setMatches(getMatches() - int(macthesValue.text))        
        matchesNumber.text = str(getMatches())


    def removeMaxTakenMatchesButtonEvent():
        currentValue = int(macthesValue.text)
        if(currentValue > 1):
            macthesValue.setText(str(currentValue - 1))



    def addMaxTakenMatchesButtonEvent():
        currentValue = int(macthesValue.text)
        if(currentValue < getMaxNumberOfMatchesTakeable()):
            macthesValue.setText(str(currentValue + 1))


        


    screen = Screen("Jeu de Nim - En jeu")
    background = Picture(0,0, "./ressources/images/background.png")
    background.resize(1280,720)
    title = Text(380,25,"A Votre Tour !",70)
    mainArea = Area(40,175,1200,500) 
    sideArea = Area(360, 25, 600, 100)

    increaseButton = Button(740,550, "+", addMaxTakenMatchesButtonEvent, 95,95)

    macthesValue = Button(600,550, "1", nullEvent, 95, 95)

    matchesNumber = Button(600,325, str(getMatches()), nullEvent,95,95, "#DED0B6", "#DED0B6")
    decreaseButton = Button(450,550, "-", removeMaxTakenMatchesButtonEvent, 95,95)  

    valideButton = Button(950,550, "Valider", validateButtonEvent, 250, 85)
    returnButton = Button(75,550, "Retour", backButtonEvent, 250, 85)


    screen.add_element(background)
    screen.add_element(mainArea)
    screen.add_element(sideArea)
    screen.add_element(title)
    screen.add_element(returnButton)
    screen.add_element(valideButton)
    screen.add_element(increaseButton)
    screen.add_element(macthesValue)
    screen.add_element(decreaseButton)
    screen.add_element(matchesNumber)

    screen.run()