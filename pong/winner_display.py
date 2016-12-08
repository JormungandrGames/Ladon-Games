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
EXIT = 0
NEW_GAME = 1
ARCADE = 2
MENU = 3


class WinnerDisplay:
    def __init__(self, screen):
        self.__screen = screen
        self.__font = pygame.font.Font('resources/fonts/SkyrimFont.ttf', (int(self.__screen.get_rect().height/FONT_MODIFIER)))

    def pause_loop(self, winner):
        # Crates the transparent surface for the menu
        temp = pygame.Surface((self.__screen.get_rect().width, self.__screen.get_rect().height))
        temp.set_alpha(ALPHA)
        temp_pos = temp.get_rect()
        temp_pos.centerx = self.__screen.get_rect().centerx
        temp_pos.centery = self.__screen.get_rect().centery

        self.__screen.blit(temp, temp_pos)

        # winner screen depending on who wins
        winnerDisplayOne = pygame.image.load("pong/resources/images/PlayerOneWins.jpg").convert_alpha()
        winnerDisplayOne = pygame.transform.scale(winnerDisplayOne, (300, 300))
        winnerDisplayOne_pos = winnerDisplayOne.get_rect()
        winnerDisplayOne_pos.centerx = self.__screen.get_rect().centerx
        winnerDisplayOne_pos.centery = self.__screen.get_rect().centery - 100

        winnerDisplayTwo = pygame.image.load("pong/resources/images/PlayerTwoWins.jpg").convert_alpha()
        winnerDisplayTwo = pygame.transform.scale(winnerDisplayTwo, (225, 225))
        winnerDisplayTwo_pos = winnerDisplayTwo.get_rect()
        winnerDisplayTwo_pos.centerx = self.__screen.get_rect().centerx
        winnerDisplayTwo_pos.centery = self.__screen.get_rect().centery - 100

        if winner == 0:
            self.__screen.blit(winnerDisplayOne, winnerDisplayOne_pos)
        if winner == 1:
            self.__screen.blit(winnerDisplayTwo, winnerDisplayTwo_pos)

        # Create the menu font/button and position
        b_game = self.__font.render('Play Again', ANTI_ANILIASING, WHITE)
        b_game_pos = b_game.get_rect()
        b_game_pos.centerx = self.__screen.get_rect().centerx
        b_game_pos.centery = self.__screen.get_rect().centery + 100

        # Create the menu font/button and position
        b_menu = self.__font.render('Menu', ANTI_ANILIASING, WHITE)
        b_menu_pos = b_menu.get_rect()
        b_menu_pos.centerx = self.__screen.get_rect().centerx
        b_menu_pos.centery = self.__screen.get_rect().centery + 150

        # Create the Arcade font/button and position
        b_arcade = self.__font.render('Arcade', ANTI_ANILIASING, WHITE)
        b_arcade_pos = b_arcade.get_rect()
        b_arcade_pos.centerx = self.__screen.get_rect().centerx - 40
        b_arcade_pos.centery = self.__screen.get_rect().centery + 200

        # Create the Quit font/button and position
        b_quit = self.__font.render('Quit', ANTI_ANILIASING, WHITE)
        b_quit_pos = b_quit.get_rect()
        b_quit_pos.centerx = self.__screen.get_rect().centerx - 65
        b_quit_pos.centery = self.__screen.get_rect().centery + 250

        # Blits the three buttons/fonts
        self.__screen.blit(b_game, b_game_pos)
        self.__screen.blit(b_menu, b_menu_pos)
        self.__screen.blit(b_quit, b_quit_pos)
        self.__screen.blit(b_arcade, b_arcade_pos)

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
            # User clicked new game, exits to new game
            elif b_game_pos.collidepoint(mouse_pos) and on_click1 == CLICKED:
                return NEW_GAME
            # User clicked exit, exits to OS
            elif b_arcade_pos.collidepoint(mouse_pos) and on_click1 == CLICKED:
                return ARCADE
            # User clicks menu goes to pong menu
            elif b_menu_pos.collidepoint(mouse_pos) and on_click1 == CLICKED:
                return MENU
            elif b_quit_pos.collidepoint(mouse_pos) and on_click1 == CLICKED:
                return EXIT

            # Updates the screen
            pygame.display.flip()
