from utils.ScreenUtils import *

def showSoloSettingsScreen():
    from ui.SoloScreen import showSoloScreen
    from common.NimGame import setMatches
    from common.NimGame import getMatches
    from common.NimGame import setMaxNumberOfMatchesTakeable
    screen = Screen("Jeu de Nim - Paramètres")
    background = Picture(0, 0, "./ressources/images/background.png")
    background.resize(1280, 720)
    settingsText = Text(530, 25, "PARAMETRES", 70)

    matchesNumberText = Text(475, 245, "Nombres\nallumettes", 30)
    maxMatchesNumberText = Text(475, 370, "Nombre prises\nmaxi", 30)
    difficultyText = Text(475, 145, "Difficulté", 30)

    def resetButtonEvent():
        numberOfMatches.setText("16")
        numberOfMaxTeakeableMatches.setText("3")
        difficulty.setText("1")

    def updateButtonEvent():

        setMatches(int(numberOfMatches.text))
        setMaxNumberOfMatchesTakeable(int(numberOfMaxTeakeableMatches.text))
        showSoloScreen()
        

        pygame.quit()

    def backButtonEvent():
        showSoloScreen()
        pygame.quit()

    def removeMatchesButtonEvent():
        currentValue = int(numberOfMatches.text)
        if(currentValue > 1):
            numberOfMatches.setText(str(currentValue - 1))
    def addMatchesButtonEvent():
        currentValue = int(numberOfMatches.text)
        if(currentValue < 50):
            numberOfMatches.setText(str(currentValue + 1))
    
    def nullEvent():
        return None

    def removeMaxTakenMatchesButtonEvent():
        currentValue = int(numberOfMaxTeakeableMatches.text)
        if(currentValue > 1):
            numberOfMaxTeakeableMatches.setText(str(currentValue - 1))
    def addMaxTakenMatchesButtonEvent():
        currentValue = int(numberOfMaxTeakeableMatches.text)
        if(currentValue < 10):
            numberOfMaxTeakeableMatches.setText(str(currentValue + 1))

    def decreaseDifficultyButtonEvent():
        currentValue = int(difficulty.text)
        if(currentValue > 1):
            difficulty.setText(str(currentValue - 1))
    def increaseDifficultyButtonEvent():
        currentValue = int(difficulty.text)
        if(currentValue < 3):
            difficulty.setText(str(currentValue + 1))

    resetButton = Button(675, 490, "Réinitialiser", resetButtonEvent, 450, 40, "#FDF7E4", "#FAEED1", 20)
    validateButton = Button(675, 565, "Valider", updateButtonEvent, 450, 95, "#FDF7E4", "#FAEED1", 40)
    returnButton = Button(525, 565, "<", backButtonEvent, 95, 95, "#FDF7E4", "#FAEED1", 40)

    decreaseDifficulty = Button(780, 120, "-", decreaseDifficultyButtonEvent, 95, 95, "#FDF7E4", "#FAEED1", 40)
    difficulty = Button(905, 120, "1", nullEvent, 95, 95, "#FDF7E4", "#FAEED1", 40)
    increaseDifficulty = Button(1035, 120, "+", increaseDifficultyButtonEvent, 95, 95, "#FDF7E4", "#FAEED1", 40)

    removeMatches = Button(780, 240, "-", removeMatchesButtonEvent, 95, 95, "#FDF7E4", "#FAEED1", 40)
    numberOfMatches = Button(905, 240, "16", nullEvent, 95, 95, "#FDF7E4", "#FAEED1", 40)
    addMatches = Button(1035, 240, "+", addMatchesButtonEvent, 95, 95, "#FDF7E4", "#FAEED1", 40)

    removeMaxTakenMatches = Button(780, 365, "-", removeMaxTakenMatchesButtonEvent, 95, 95, "#FDF7E4", "#FAEED1", 40)
    numberOfMaxTeakeableMatches = Button(905, 365, "3", nullEvent, 95, 95, "#FDF7E4", "#FAEED1", 40)
    addMaxTakenMatches = Button(1035, 365, "+", addMaxTakenMatchesButtonEvent, 95, 95, "#FDF7E4", "#FAEED1", 40)

    settingsArea = Area(425, 10, 750, 690)

    screen.add_element(background)
    screen.add_element(settingsArea)
    screen.add_element(settingsText)
    screen.add_element(difficultyText)
    screen.add_element(matchesNumberText)
    screen.add_element(maxMatchesNumberText)

    screen.add_element(resetButton)
    screen.add_element(validateButton)
    screen.add_element(returnButton)

    screen.add_element(increaseDifficulty)
    screen.add_element(difficulty)
    screen.add_element(decreaseDifficulty)

    screen.add_element(removeMatches)
    screen.add_element(addMatches)
    screen.add_element(numberOfMatches)

    screen.add_element(removeMaxTakenMatches)
    screen.add_element(addMaxTakenMatches)
    screen.add_element(numberOfMaxTeakeableMatches)

    screen.run()