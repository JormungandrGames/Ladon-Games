import pygame

# COLORS
WHITE = (250, 250, 250)
BLACK = (0, 0, 0)

# SCREEN AND FONT MODIFIERS
ANTI_ANILIASING = 1
FONT_MODIFIER = 15
EXIT_TO_MENU = 0
EXIT_GAME = 1
ALPHA = 150
CLICKED = 1
EXIT = 2
MENU = 3


class Controls:
    def __init__(self, screen):
        self.__screen = screen
        self.__font = pygame.font.Font('resources/fonts/SkyrimFont.ttf', (int(self.__screen.get_rect().height/FONT_MODIFIER)))

    def control_loop(self):

        # winner screen depending on who wins
        HelpScreen = pygame.image.load("pong/resources/images/controls.png").convert_alpha()
        HelpScreen = pygame.transform.scale(HelpScreen, (self.__screen.get_rect().width, self.__screen.get_rect().height))
        HelpScreen_pos = HelpScreen.get_rect()
        HelpScreen_pos.centerx = self.__screen.get_rect().centerx
        HelpScreen_pos.centery = self.__screen.get_rect().centery

        self.__screen.blit(HelpScreen, HelpScreen_pos)

        # Create the menu font/button and position
        b_menu = self.__font.render('Menu', ANTI_ANILIASING, BLACK)
        b_menu_pos = b_menu.get_rect()
        b_menu_pos.centerx = self.__screen.get_rect().centerx - 100
        b_menu_pos.centery = self.__screen.get_rect().centery + 300

        # Create the Quit font/button and position
        b_quit = self.__font.render('Quit', ANTI_ANILIASING, BLACK)
        b_quit_pos = b_quit.get_rect()
        b_quit_pos.centerx = self.__screen.get_rect().centerx + 100
        b_quit_pos.centery = self.__screen.get_rect().centery + 300

        # Blits the three buttons/fonts
        self.__screen.blit(b_menu, b_menu_pos)
        self.__screen.blit(b_quit, b_quit_pos)

        paused = True

        while paused:
            pygame.event.clear()

            # Gets the mouse position
            mouse_pos = pygame.mouse.get_pos()
            (on_click1, on_click2, on_click3) = pygame.mouse.get_pressed()

            # Peeks into the queued peek events
            event = pygame.event.peek()

            # Exit
            if event.type == pygame.QUIT:
                return EXIT
            # User clicks menu goes to pong menu
            elif b_menu_pos.collidepoint(mouse_pos) and on_click1 == CLICKED:
                return MENU
            elif b_quit_pos.collidepoint(mouse_pos) and on_click1 == CLICKED:
                return EXIT

            # Updates the screen
            pygame.display.flip()
