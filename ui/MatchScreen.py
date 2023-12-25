from utils.ScreenUtils import *
import random

def showMatchScreen(screen):
    from common.NimGame import getMaxNumberOfMatchesTakeable
    from common.NimGame import getMatches
    from common.NimGame import setMatches
    from common.NimGame import getDifficulty
    from common.NimGame import getMode
    from common.NimGame import getFirstPlayerName
    from common.NimGame import getSecondPlayerName
    from ui.MainScreen import showMainScreen
    from common.NimGame import initValues

    screen.clear_elements()
    background = Picture(0, 0, "./ressources/images/background.png")
    background.resize(1280, 720)
    if(getMode() == 1):
        current_turn = 1
        sideArea = Area(360, 25, 600, 100)
        title = Text(380, 25, "A Votre Tour !", 70)
    elif(getMode() == 2):
        current_turn = random.randint(0,1)
        sideArea = Area(150, 25, 1000, 100)
        if(current_turn == 0):
            title = Text(190, 35, ("Au tour de " + getSecondPlayerName()), 50)
        else:
            title = Text(190, 35, ("Au tour de " + getFirstPlayerName()), 50)
    mainArea = Area(40, 175, 1200, 500)
    

    def nullEvent():
        return None

    def calculateNimSum():
        matches = getMatches()
        max_takeable = getMaxNumberOfMatchesTakeable()

        if matches % (max_takeable + 1) == 0:
            return 0
        else:
            return matches % (max_takeable + 1)

    def botTurn():
        nonlocal current_turn
        if getMode() == 1:
            if getDifficulty() == 1:  # Easy mode
                if getMatches() > 0:
                    matchesTaken = min(random.randint(1, getMatches()), getMaxNumberOfMatchesTakeable())
                    setMatches(getMatches() - matchesTaken)
                    matchesNumber.text = str(getMatches())
                    checkGameResult()
                    current_turn = 1  # Changer le tour après que l'IA a joué
                    
            elif getDifficulty() == 2:  # Medium mode
                if getMatches() > 0:
                    # Utiliser une approche probabiliste
                    if random.random() < 0.7:  # 70% de chances de jouer de manière aléatoire
                        matchesTaken = min(random.randint(1, getMatches()), getMaxNumberOfMatchesTakeable())
                    else:
                        # Calculer le nim-sum
                        nim_sum = calculateNimSum()

                        # Si le nim-sum est non nul, jouer de manière intelligente
                        if nim_sum != 0:
                            matchesTaken = getMatches() % (getMaxNumberOfMatchesTakeable() + 1)
                        else:
                            # Sinon, jouer de manière aléatoire
                            matchesTaken = min(random.randint(1, getMatches()), getMaxNumberOfMatchesTakeable())

                    setMatches(getMatches() - matchesTaken)
                    matchesNumber.text = str(getMatches())
                    checkGameResult()
                    current_turn = 1  # Changer le tour après que l'IA a joué
            else:  # Hard mode
                if getMatches() > 0:
                    if getMatches() == 1:
                        matchesTaken = 1
                    else:
                        matchesTaken = getMatches() % (getMaxNumberOfMatchesTakeable() + 1)

                        # Si nim-sum est 0, jouer de manière aléatoire
                        if calculateNimSum() == 0:
                            matchesTaken = random.randint(1, min(getMatches(), getMaxNumberOfMatchesTakeable()))

                    setMatches(getMatches() - matchesTaken)
                    matchesNumber.text = str(getMatches())
                    checkGameResult()
                    current_turn = 1

    def homeButtonEvent():
        initValues()
        showMainScreen(screen)

    def checkGameResult():
            if getMatches() == 0:
                accueil = Button(475, 550, "Accueil", homeButtonEvent)
                menuArea = Area(40, 525, 1200, 150)
                title.setText(" ")
                screen.add_element(menuArea)
                screen.add_element(accueil)
                if(getMode() == 1):
                    looseText = Text(515, 35, "Perdu ! :(",50, )
                    winText = Text(515, 35, "Gagné ! :D",50, )
                    if current_turn == 0:
                        screen.add_element(winText)
                    else:
                        screen.add_element(looseText)
                elif(getMode() == 2):
                    if(current_turn == 0):
                        winText = Text(190, 35, ("Victoire de " + getFirstPlayerName()),50)
                    else:
                        winText = Text(190, 35, ("Victoire de " + getSecondPlayerName()),50)
                    screen.add_element(winText)
                

    def backButtonEvent():
        initValues()
        showMainScreen(screen)

    def validateButtonEvent():
        nonlocal current_turn
        if(getMode() == 1):
            if title.text == "A Votre Tour !":
                playerMatchesTaken = int(matchesValue.text)
                setMatches(getMatches() - playerMatchesTaken)
                matchesNumber.text = str(getMatches())
                matchesValue.text = "1"
                checkGameResult()
                current_turn = 2 # Changer le tour après que le joueur a joué
                botTurn()
        elif(getMode() == 2):
            playerMatchesTaken = int(matchesValue.text)
            setMatches(getMatches() - playerMatchesTaken)
            matchesNumber.text = str(getMatches())
            matchesValue.text = "1"
            if(current_turn == 1):
                title.text = ("Au tour de " + getSecondPlayerName())
                checkGameResult()
                current_turn = 0
            else:
                title.text = ("Au tour de " + getFirstPlayerName())
                checkGameResult()
                current_turn = 1
            

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
