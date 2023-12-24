from utils.ScreenUtils import *
import random

def showMatchScreen(screen):
    from ui.SoloScreen import showSoloScreen
    from ui.SoloSettingsScreen import showSoloSettingsScreen
    from common.NimGame import getMaxNumberOfMatchesTakeable
    from common.NimGame import setMaxNumberOfMatchesTakeable
    from common.NimGame import getMatches
    from common.NimGame import setMatches
    from common.NimGame import getDifficulty
    from common.NimGame import setDifficulty
    from ui.MainScreen import showMainScreen
    from ui.LoadingScreen import showLoadingScreen

    screen.clear_elements()
    background = Picture(0, 0, "./ressources/images/background.png")
    background.resize(1280, 720)
    title = Text(380, 25, "A Votre Tour !", 70)
    mainArea = Area(40, 175, 1200, 500)
    sideArea = Area(360, 25, 600, 100)

    def nullEvent():
        return None
    
    def botTurn():
        pygame.time.wait(1000)
        if getDifficulty() == 1:
            if getMatches() > 0:
                matchesTaken = min(random.randint(1, getMatches()), getMaxNumberOfMatchesTakeable())
                setMatches(getMatches() - matchesTaken)
                matchesNumber.text = str(getMatches())
                #title.setText("A Votre Tour !")
                pygame.display.flip()
    
    def checkGameResult():
        if getMatches() == 0:
            if title.text == "Tour de l'IA":
                title.setText("Vous avez gagné !")
            else:
                title.setText("L'IA a gagné !")


    def backButtonEvent():
        showMainScreen(screen)

    def validateButtonEvent():
        playerMatchesTaken = int(matchesValue.text)
        setMatches(getMatches() - playerMatchesTaken)
        matchesNumber.text = str(getMatches())
        matchesValue.text = "1"
        checkGameResult()
        title.setText("Tour de l'IA")
        botTurn()
        checkGameResult()


    def removeMaxTakenMatchesButtonEvent():
        currentValue = int(matchesValue.text)
        if currentValue > 1:
            matchesValue.setText(str(currentValue - 1))

    def addMaxTakenMatchesButtonEvent():
        currentValue = int(matchesValue.text)
        if currentValue < getMaxNumberOfMatchesTakeable():
            if currentValue < getMatches():
                matchesValue.setText(str(currentValue + 1))



    increaseButton = Button(740, 550, "+", addMaxTakenMatchesButtonEvent, 95, 95)
    matchesValue = Button(600, 550, "1", nullEvent, 95, 95)
    matchesNumber = Button(600, 325, str(getMatches()), nullEvent, 95, 95, "#DED0B6", "#DED0B6")
    decreaseButton = Button(450, 550, "-", removeMaxTakenMatchesButtonEvent, 95, 95)
    validateButton = Button(950, 550, "Valider", validateButtonEvent, 250, 85)
    returnButton = Button(75, 550, "Retour", backButtonEvent, 250, 85)

    screen.add_element(background)
    screen.add_element(mainArea)
    screen.add_element(sideArea)
    screen.add_element(title)
    screen.add_element(returnButton)
    screen.add_element(validateButton)
    screen.add_element(increaseButton)
    screen.add_element(matchesValue)
    screen.add_element(decreaseButton)
    screen.add_element(matchesNumber)

    screen.run()


