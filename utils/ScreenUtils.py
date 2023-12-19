import pygame

class Screen:
    """
    Class permettant de créer des fenêtre pygame.

    Paramètres:
    * Title: Titre de la fenêtre
    * Width: Largeur de la fenêtre (défaut 1280px)
    * Height: Hauteur de la fenêtre (défaut 720px)

    Méthodes:
    * add_element: Ajoute un élément à la fenêtre
    * run: Lance la fenêtre
    """

    def __init__(self, title, width=1280, height=720):
        """
        Initialise la fenêtre.
        """
        self.width = width
        self.height = height
        self.title = title
        self.elements = []

        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()

    def add_element(self, element):
        """
        Ajoute un élément à la fenêtre.

        Paramètres:
        * element: Element à ajouter
        """
        self.elements.append(element)

    def run(self):
        """
        Lance la fenêtre.
        """
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for element in self.elements:
                        if isinstance(element, Button) and element.isMouseOver():
                            element.handle_click()

            self.screen.fill((255, 255, 255))

            for element in self.elements:
                element.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(60)

class Button:
    """
    Class permettant de créer des boutons pour une fenêtre Pygame.

    Paramètres:
    * x: Position x du bouton
    * y: Position y du bouton
    * text: Texte du bouton
    * click_handler: Fonction appelée lors du clic sur le bouton
    * width: Largeur du bouton (défaut 325px)
    * height: Hauteur du bouton (défaut 85px)
    * button_color: Couleur du bouton (défaut #FDF7E4)
    * shadow_color: Couleur de l'ombre du bouton (défaut #FAEED1)
    * font_size: Taille de la police du texte (défaut 45px)

    Méthodes:
    * draw: Dessine le bouton
    * isMouseOver: Renvoie True si la souris est sur le bouton
    * handle_click: Appelle la fonction click_handler si la souris est sur le bouton
    """
    def __init__(self, x, y, text, click_handler, width=325, height=85, button_color="#FDF7E4", shadow_color="#FAEED1", font_size=45):
        """
        Initialise le bouton.
        """
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text.upper()
        self.font = pygame.font.Font("./ressources/fonts/BowlbyOne-Regular.ttf", font_size)
        self.button_color = pygame.Color(button_color)
        self.shadow_color = pygame.Color(shadow_color)
        self.click_handler = click_handler

    def draw(self, screen):
        """
        Dessine le bouton.
        
        Paramètres:
        * screen: Fenêtre sur laquelle dessiner le bouton
        """
        shadow_rect = pygame.Rect(self.rect.x + 10, self.rect.y + 10, self.rect.width, self.rect.height)
        pygame.draw.rect(screen, self.shadow_color, shadow_rect)

        pygame.draw.rect(screen, self.button_color, self.rect)

        text_surface = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)

        shadow_surface = pygame.Surface((text_rect.width, text_rect.height), pygame.SRCALPHA)

        shadow_surface.blit(self.font.render(self.text, True, (120, 120, 120,)), (0, 1))

        screen.blit(shadow_surface, (text_rect.x + 2, text_rect.y + 2))

        screen.blit(text_surface, text_rect)

    def isMouseOver(self):
        """
        Renvoie True si la souris est sur le bouton.
        
        Retour:
        * True si la souris est sur le bouton
        * False sinon
        """
        return self.rect.collidepoint(pygame.mouse.get_pos())
    
    def handle_click(self):
        """
        Appelle la fonction click_handler si la souris est sur le bouton.
        """
        if self.click_handler:
            self.click_handler()

    def setText(self, text):
        """
        Change le texte du bouton.

        Paramètres:
        * text: Nouveau texte à afficher
        """
        self.text = text.upper()


class Area:
    """
    Class permettant de créer des zones de couleurs pour une fenêtre Pygame.

    Paramètres:
    * x: Position x de la zone
    * y: Position y de la zone
    * width: Largeur de la zone
    * height: Hauteur de la zone
    * background_color: Couleur de fond de la zone (défaut #DED0B6)
    * shadow_color: Couleur de l'ombre de la zone (défaut #BBAB8C)

    Méthodes:
    * draw: Dessine la zone
    """
    def __init__(self, x, y, width, height, background_color="#DED0B6", shadow_color="#BBAB8C"):
        """
        Initialise la zone de couleur.
        """
        self.rect = pygame.Rect(x, y, width, height)
        self.background_color = pygame.Color(background_color)
        self.shadow_color = pygame.Color(shadow_color)

    def draw(self, screen):
        """
        Dessine la zone de couleur.
        
        Paramètres:
        * screen: Fenêtre sur laquelle dessiner la zone
        """
        shadow_rect = pygame.Rect(self.rect.x + 10, self.rect.y + 10, self.rect.width, self.rect.height)
        pygame.draw.rect(screen, self.shadow_color, shadow_rect)
        pygame.draw.rect(screen, self.background_color, self.rect)

class Text:
    """
    Class permettant d'ajouter du texte à une fenêtre Pygame rapidement.

    Paramètres:
    * x: Position x du texte
    * y: Position y du texte
    * text: Texte à afficher
    * font_size: Taille de la police du texte (défaut 50px)
    * color: Couleur du texte (défaut #FFFFFF)

    Méthodes:
    * draw: Dessine le texte
    * setText: Change le texte
    """
    def __init__(self, x, y, text, font_size=50, color=(255, 255, 255)):
        """
        Initialise le texte.
        """
        self.x = x
        self.y = y
        self.text = text
        self.font = pygame.font.Font("./ressources/fonts/BowlbyOne-Regular.ttf", font_size)
        self.color = color

    def setText(self, text):
        """
        Change le texte.

        Paramètres:
        * text: Nouveau texte à afficher
        """
        self.text = text

    def draw(self, screen):
        """
        Dessine le texte.
        """
        text_surface = self.font.render(self.text, True, self.color)
        text_rect = text_surface.get_rect(topleft=(self.x, self.y))
        screen.blit(text_surface, text_rect)

class Picture:
    """
    Class permettant d'ajouter des images à une fenêtre Pygame rapidement.

    Paramètres:
    * x: Position x de l'image
    * y: Position y de l'image
    * image_path: Chemin vers l'image

    Méthodes:
    * draw: Dessine l'image
    * resize: Redimensionne l'image
    """
    def __init__(self, x, y, image_path):
        """
        Initialise l'image.
        """
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_path)

    def draw(self, screen):
        """
        Dessine l'image.
        
        Paramètres:
        * screen: Fenêtre sur laquelle dessiner l'image
        """
        screen.blit(self.image, (self.x, self.y))

    def resize(self, width, height):
        """
        Redimensionne l'image.

        Paramètres:
        * width: Nouvelle largeur de l'image
        * height: Nouvelle hauteur de l'image
        """
        self.image = pygame.transform.scale(self.image, (width, height))

class InputBox:
    def __init__(self, x, y, width, height, font_size=30, text_color=(0, 0, 0), border_color=(253, 247, 228)):
        self.rect = pygame.Rect(x, y, width, height)
        self.font = pygame.font.Font(None, font_size)
        self.text_color = text_color
        self.border_color = border_color
        self.text = ''
        self.active = False
        self.max_length = 12  # Longueur maximale du texte

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
        elif event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.active = False
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    # Vérification de la longueur maximale et des caractères spéciaux
                    if len(self.text) < self.max_length and event.unicode.isalnum() or event.unicode == '_':
                        self.text += event.unicode

    def draw(self, screen):
        pygame.draw.rect(screen, self.border_color, self.rect, 2)
        font_surface = self.font.render(self.text, True, self.text_color)
        width = max(self.rect.width, font_surface.get_width() + 10)
        input_box_rect = pygame.Rect(self.rect.x, self.rect.y, width, self.rect.height)
        screen.blit(font_surface, (self.rect.x + 5, self.rect.y + 5))
        pygame.draw.rect(screen, self.border_color, input_box_rect, 2)

    def get_text(self):
        return self.text

    def is_empty(self):
        return len(self.text) == 0

    def contains_special_characters(self):
        return any(char.isalnum() or char == '_' for char in self.text)