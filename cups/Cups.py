import pygame
from random import randint
from pause_menu import *
from menu import *


#
# SKIP TO LINE 107 FOR PAUSE MENU
#

# COLORS CONSTANTS
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# SCREEN, FONT AND MUSIC CONSTANTS
ANTI_ANILIASING = 1
LOOP_MUSIC = -1
RAND_RANGE_ONE = 1
RAND_RANGE_TWO = 3
FONT_MODIFIER = 15
CLICKED = 1

# POSITION CONSTANTS
EXIT_SIZE = (40, 40)
CUP_ONE_X = 100
CUP_TWO_X = 400
CUP_THREE_X = 200
OUTER_CUPS_Y = 200
INNER_CUP_Y = 50
CUP_SIZE_X = 200
CUP_SIZE_Y = 300
RECT_WIDTH = 1
TEXT_Y = 300
TEXT_SIZE = 50


class Cups:
    def __init__(self, screen):
        # Screen surface
        self.__screen = screen

        # Running game
        self.__running = True

        # Init Music
        self.__music = pygame.mixer.music.load('cups/resources/music/YodaSong.mp3')

        # Load Font
        self.__font = pygame.font.Font('cups/resources/fonts/NIAGENG.TTF',
                                       int(self.__screen.get_rect().height/FONT_MODIFIER))

    def game_loop(self):
        # Loads the music, -1 means loop it forever
        pygame.mixer.music.play(LOOP_MUSIC)

        # Reload the cups and font
        restart = False
        rand = None

        # Call pause
        pause = Pause(self.__screen)
        pause_options = None
        self.__running = True

        # Game Loop
        while self.__running:
            # Clears the screen and fills it with color (black)
            if restart is False:
                self.__screen.fill(BLACK)

            # Load the cups - sorry this is a mess
            cup_two = pygame.draw.rect(self.__screen, RED, (self.__screen.get_rect().centerx - CUP_ONE_X,
                                                            (self.__screen.get_rect().centery - INNER_CUP_Y),
                                                            CUP_SIZE_X, CUP_SIZE_Y), RECT_WIDTH)
            cup_one = pygame.draw.rect(self.__screen, RED, (cup_two.centerx - CUP_TWO_X,
                                                            (self.__screen.get_rect().centery - OUTER_CUPS_Y),
                                                            CUP_SIZE_X, CUP_SIZE_Y), RECT_WIDTH)
            cup_three = pygame.draw.rect(self.__screen, RED, (cup_two.centerx + CUP_THREE_X,
                                                              (self.__screen.get_rect().centery - OUTER_CUPS_Y),
                                                              CUP_SIZE_X, CUP_SIZE_Y), RECT_WIDTH)

            # Get mouse clicks
            mouse_pos = pygame.mouse.get_pos()
            (on_click1, on_click2, on_click3) = pygame.mouse.get_pressed()

            # On mouse and keyboard events
            for event in pygame.event.get():
                # Hit quit
                if event.type == pygame.QUIT:
                    self.__running = False
                # Space bar to set the bool to true to reset
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    restart = False
                    rand = None
                # Check for cup one click
                elif cup_one.collidepoint(mouse_pos) & on_click1 == CLICKED and restart is False:
                    rand = randint(RAND_RANGE_ONE, RAND_RANGE_TWO)
                    restart = True
                # Check for cup two click
                elif cup_two.collidepoint(mouse_pos) & on_click1 == CLICKED and restart is False:
                    rand = randint(RAND_RANGE_ONE, RAND_RANGE_TWO)
                    restart = True
                # Check for cup three click
                elif cup_three.collidepoint(mouse_pos) & on_click1 == CLICKED and restart is False:
                    rand = randint(RAND_RANGE_ONE, RAND_RANGE_TWO)
                    restart = True

                # Get escape key press for menu; COPY THIS BLOCK FOR PAUSE MENU
                elif pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    pause_options = pause.pause_loop()
                    if pause_options == 0:
                        self.__running = False
                        return True
                    elif pause_options == 1:
                        self.__running = False

                if rand == 1:
                    win = self.__font.render("You Win!", ANTI_ANILIASING, BLUE)
                    self.__screen.blit(win, (cup_one.centerx, cup_one.centery - TEXT_Y, TEXT_SIZE, TEXT_SIZE))
                elif rand is not None:
                    lose = self.__font.render("You Lose :(", ANTI_ANILIASING, BLUE)
                    self.__screen.blit(lose, (cup_one.centerx, cup_one.centery - TEXT_Y, TEXT_SIZE, TEXT_SIZE))

            # Updates the screen
            pygame.display.flip()
