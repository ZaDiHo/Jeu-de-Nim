from utils.ScreenUtils import *

def showLocalSettingsScreen(screen):
    from ui.LocalScreen import showLocalScreen

    screen.clear_elements()
    background = Picture(0, 0, "./ressources/images/background.png")
    background.resize(1280, 720)
    settingsText = Text(530, 60, "PARAMETRES", 70)

    matchesNumberText = Text(475, 200, "Nombres\nallumettes", 30)
    maxMatchesNumberText = Text(475, 325, "Nombre prises\nmaxi", 30)

    def resetButtonEvent():
        numberOfMatches.setText("16")
        numberOfMaxTeakeableMatches.setText("3")

    def updateButtonEvent():
        print("validate")

    def backButtonEvent():
        showLocalScreen(screen)

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

    resetButton = Button(675, 475, "Réinitialiser", resetButtonEvent, 450, 40, "#FDF7E4", "#FAEED1", 20)
    validateButton = Button(675, 550, "Valider", updateButtonEvent, 450, 95, "#FDF7E4", "#FAEED1", 40)
    returnButton = Button(525, 550, "<", backButtonEvent, 95, 95, "#FDF7E4", "#FAEED1", 40)

    removeMatches = Button(780, 200, "-", removeMatchesButtonEvent, 95, 95, "#FDF7E4", "#FAEED1", 40)
    numberOfMatches = Button(905, 200, "16", nullEvent, 95, 95, "#FDF7E4", "#FAEED1", 40)
    addMatches = Button(1035, 200, "+", addMatchesButtonEvent, 95, 95, "#FDF7E4", "#FAEED1", 40)

    removeMaxTakenMatches = Button(780, 325, "-", removeMaxTakenMatchesButtonEvent, 95, 95, "#FDF7E4", "#FAEED1", 40)
    numberOfMaxTeakeableMatches = Button(905, 325, "3", nullEvent, 95, 95, "#FDF7E4", "#FAEED1", 40)
    addMaxTakenMatches = Button(1035, 325, "+", addMaxTakenMatchesButtonEvent, 95, 95, "#FDF7E4", "#FAEED1", 40)

    settingsArea = Area(425, 50, 750, 625)

    screen.add_element(background)
    screen.add_element(settingsArea)
    screen.add_element(settingsText)
    screen.add_element(matchesNumberText)
    screen.add_element(maxMatchesNumberText)

    screen.add_element(resetButton)
    screen.add_element(validateButton)
    screen.add_element(returnButton)

    screen.add_element(removeMatches)
    screen.add_element(addMatches)
    screen.add_element(numberOfMatches)

    screen.add_element(removeMaxTakenMatches)
    screen.add_element(addMaxTakenMatches)
    screen.add_element(numberOfMaxTeakeableMatches)

    screen.run()