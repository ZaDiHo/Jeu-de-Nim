from utils.ScreenUtils import *
    
def showLocalScreen(screen):
    from ui.MainScreen import showMainScreen
    from ui.LocalSettingsScreen import showLocalSettingsScreen
    from common.NimGame import getFirstPlayerName
    from common.NimGame import getSecondPlayerName
    from common.NimGame import setFirstPlayerName
    from common.NimGame import setSecondPlayerName
    from ui.MatchScreen import showMatchScreen

    screen.clear_elements()

    background = Picture(0,0, "./ressources/images/background.png")
    background.resize(1280,720)

    title = Text(810,85,"LOCAL",70,)
    vsText = Text(250, 295, "CONTRE", 40)
    firstPlayerName = InputBox(230, 255, 300, 40, 40, (255,255,255), "#DED0B6")
    secondPlayerName = InputBox(230, 375, 300, 40, 40, (255,255,255), "#DED0B6")
    firstPlayerName.text = getFirstPlayerName()
    secondPlayerName.text = getSecondPlayerName()
    firstPlayerText = Text(190, 250, "1. _________________", 30)
    secondPlayerText = Text(190, 370, "2. _________________", 30)
    menuArea = Area(650,75,550,550)
    nameArea = Area(100, 205, 500, 250)

    def settingsButtonEvent():
        setFirstPlayerName(firstPlayerName.text)
        setSecondPlayerName(secondPlayerName.text)
        showLocalSettingsScreen(screen)
        
    def startButtonEvent():
        setFirstPlayerName(firstPlayerName.text)
        setSecondPlayerName(secondPlayerName.text)
        showMatchScreen(screen)

    def backButtonEvent():
        showMainScreen(screen)

    settingsButton = Button(710,190,"Parametres",settingsButtonEvent,425,105)
    startButton = Button(710,325,"Lancer !",startButtonEvent,425,105)
    backButton = Button(710,460,"Retour",backButtonEvent,425,105)

    
    screen.add_element(background)
    screen.add_element(menuArea)
    screen.add_element(settingsButton)
    screen.add_element(startButton)
    screen.add_element(backButton)
    screen.add_element(title)
    screen.add_element(nameArea)
    screen.add_element(vsText)
    screen.add_element(firstPlayerText)
    screen.add_element(secondPlayerText)
    screen.add_element(firstPlayerName)
    screen.add_element(secondPlayerName)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                firstPlayerName.handle_event(event)
                secondPlayerName.handle_event(event)
                if settingsButton.isMouseOver():
                    settingsButton.handle_click()
                elif startButton.isMouseOver():
                    startButton.handle_click()
                elif backButton.isMouseOver():
                    backButton.handle_click()
            elif event.type == pygame.KEYDOWN:
                firstPlayerName.handle_event(event)
                secondPlayerName.handle_event(event)

        # Dessiner les éléments
        screen.screen.fill((255, 255, 255))
        for element in screen.elements:
            element.draw(screen.screen)

        pygame.display.flip()
        screen.clock.tick(60)


    
    screen.run()

