# Nom du fichier: LocalSettingsScreen.py
# Auteur: Abdelrahman AL KHATIB
# Objectif: Ecran des paramètres du jeu local
# Date dernière modification: 25/01/2021
# Version: 1.2

from utils.ScreenUtils import *

def showLocalSettingsScreen(screen):
    """
    Affiche l'écran des paramètres du jeu local

    Paramètres:
    * screen: l'écran sur lequel afficher les éléments
    """
    # Import des fonctions de manière locale pour éviter les dépendances circulaires
    from ui.LocalScreen import showLocalScreen
    from common.NimGame import getMaxNumberOfMatchesTakeable
    from common.NimGame import getMatches
    from common.NimGame import setMaxNumberOfMatchesTakeable
    from common.NimGame import setMatches

    # Nettoyer l'écran
    screen.clear_elements()

    # Ajout du fond de fenêtre
    background = Picture(0, 0, "./ressources/images/background.png")
    background.resize(1280, 720)

    # Création des éléments
    settingsText = Text(530, 60, "PARAMETRES", 70)
    matchesNumberText = Text(475, 200, "Nombres\nallumettes", 30)
    maxMatchesNumberText = Text(475, 325, "Nombre prises\nmaxi", 30)

    settingsArea = Area(425, 50, 750, 625)

    # Définition des événements des boutons
    def resetButtonEvent():
        """
        Réinitialise les paramètres du jeu
        """
        numberOfMatches.setText("21")
        numberOfMaxTeakeableMatches.setText("3")

    def updateButtonEvent():
        """
        Met à jour les paramètres du jeu
        """
        setMatches(int(numberOfMatches.text))
        setMaxNumberOfMatchesTakeable(int(numberOfMaxTeakeableMatches.text))
        showLocalScreen(screen)

    def backButtonEvent():
        """
        Retourne à l'écran de jeu local
        """
        showLocalScreen(screen)

    def removeMatchesButtonEvent():
        """
        Diminue le nombre d'allumettes
        """
        currentValue = int(numberOfMatches.text)
        if(currentValue > 1):
            numberOfMatches.setText(str(currentValue - 1))

    def addMatchesButtonEvent():
        """
        Augmente le nombre d'allumettes
        """
        currentValue = int(numberOfMatches.text)
        if(currentValue < 50):
            numberOfMatches.setText(str(currentValue + 1))
    
    def nullEvent():
        """
        Ne fait rien
        """
        return None

    def removeMaxTakenMatchesButtonEvent():
        """
        Diminue le nombre d'allumettes maximum pouvant être prises
        """
        currentValue = int(numberOfMaxTeakeableMatches.text)
        if(currentValue > 1):
            numberOfMaxTeakeableMatches.setText(str(currentValue - 1))

    def addMaxTakenMatchesButtonEvent():
        """
        Augmente le nombre d'allumettes maximum pouvant être prises
        """
        currentValue = int(numberOfMaxTeakeableMatches.text)
        if(currentValue < 10):
            numberOfMaxTeakeableMatches.setText(str(currentValue + 1))

    # Création des boutons
    resetButton = Button(675, 475, "Réinitialiser", resetButtonEvent, 450, 40, "#FDF7E4", "#FAEED1", 20)
    validateButton = Button(675, 550, "Valider", updateButtonEvent, 450, 95, "#FDF7E4", "#FAEED1", 40)
    returnButton = Button(525, 550, "<", backButtonEvent, 95, 95, "#FDF7E4", "#FAEED1", 40)

    removeMatches = Button(780, 200, "-", removeMatchesButtonEvent, 95, 95, "#FDF7E4", "#FAEED1", 40)
    numberOfMatches = Button(905, 200, str(getMatches()), nullEvent, 95, 95, "#FDF7E4", "#FAEED1", 40)
    addMatches = Button(1035, 200, "+", addMatchesButtonEvent, 95, 95, "#FDF7E4", "#FAEED1", 40)

    removeMaxTakenMatches = Button(780, 325, "-", removeMaxTakenMatchesButtonEvent, 95, 95, "#FDF7E4", "#FAEED1", 40)
    numberOfMaxTeakeableMatches = Button(905, 325, str(getMaxNumberOfMatchesTakeable()), nullEvent, 95, 95, "#FDF7E4", "#FAEED1", 40)
    addMaxTakenMatches = Button(1035, 325, "+", addMaxTakenMatchesButtonEvent, 95, 95, "#FDF7E4", "#FAEED1", 40)

    # Ajout des éléments à l'écran
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

    # Lancer la fenêtre
    screen.run()