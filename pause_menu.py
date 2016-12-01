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
HALF = 2


class Pause:
    def __init__(self, screen):
        self.__screen = screen
        self.__font = pygame.font.Font('resources/fonts/SkyrimFont.ttf', (int(self.__screen.get_rect().height/FONT_MODIFIER)))

    def pause_loop(self):
        # Crates the transparent surface for the menu
        temp = pygame.Surface((self.__screen.get_rect().width, self.__screen.get_rect().height))
        temp.set_alpha(ALPHA)

        # Create the return font/button and position
        self.__screen.blit(temp, self.__screen.get_rect())
        b_return = self.__font.render('Return', ANTI_ANILIASING, WHITE)
        b_return_pos = b_return.get_rect()
        b_return_pos.centerx = self.__screen.get_rect().centerx
        b_return_pos.centery = self.__screen.get_rect().centery - (self.__screen.get_rect().centery/HALF)

        # Create the menu font/button and position
        b_menu = self.__font.render('Menu', ANTI_ANILIASING, WHITE)
        b_menu_pos = b_menu.get_rect()
        b_menu_pos.centerx = self.__screen.get_rect().centerx
        b_menu_pos.centery = self.__screen.get_rect().centery

        # Create the quit font/button and position
        b_quit = self.__font.render('Quit', ANTI_ANILIASING, WHITE)
        b_quit_pos = b_quit.get_rect()
        b_quit_pos.centerx = self.__screen.get_rect().centerx
        b_quit_pos.centery = self.__screen.get_rect().centery + (self.__screen.get_rect().centery/HALF)

        # Blits the three buttons/fonts
        self.__screen.blit(b_return, b_return_pos)
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
                return
            # User clicked return, returns to game
            elif b_return_pos.collidepoint(mouse_pos) and on_click1 == CLICKED:
                return
            # User clicked menu, exits to menu
            elif b_menu_pos.collidepoint(mouse_pos) and on_click1 == CLICKED:
                return EXIT_TO_MENU
            # User clicked exit, exits to OS
            elif b_quit_pos.collidepoint(mouse_pos) and on_click1 == CLICKED:
                return EXIT_GAME

            # Updates the screen
            pygame.display.flip()
