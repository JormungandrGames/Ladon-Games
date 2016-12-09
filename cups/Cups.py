from random import randint
from game_skeleton import game_skeleton
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

# GREG
GREG_SIZE_X = 200
GREG_SIZE_Y = 150

# POSITION CONSTANTS
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
SCORE_X = 280


class Cups(game_skeleton.Game_Skeleton):
    def __init__(self, screen):
        # Loads the music, -1 means loop it forever
        # Music must be initialized before the game skeleton
        self.__music = pygame.mixer.music.load('cups/resources/music/YodaSong.ogg')
        pygame.mixer.music.play(LOOP_MUSIC)

        # Screen surface
        self.__game_skeleton = game_skeleton.Game_Skeleton(screen)
        self.__screen = screen
        self.__screen.get_rect().height = self.__game_skeleton.get_game_height()

        # Running game
        self.__running = True

        # Load Font
        self.__font = pygame.font.Font('cups/resources/fonts/NIAGENG.TTF',
                                       int(self.__screen.get_rect().height/FONT_MODIFIER))

        self.__game_title = "Cups"

        self.__score = 0

    def game_loop(self):
        # Greg
        greg = pygame.image.load('cups/resources/images/greg.png').convert_alpha()
        greg = pygame.transform.scale(greg, (GREG_SIZE_X, GREG_SIZE_Y))
        greg_pos = greg.get_rect()

        # Reload the cups and font
        restart = False
        rand = None

        # Call pause
        pause_options = None
        self.__running = True
        count = 0

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

            # Blits the game bar
            self.__game_skeleton.blit_game_bar(self.__game_title, self.__score)

            # Get mouse clicks
            mouse_pos = pygame.mouse.get_pos()
            (on_click1, on_click2, on_click3) = pygame.mouse.get_pressed()
            cup_num = 0
            # On mouse and keyboard events
            for event in pygame.event.get():
                # Check for Pause menu events, and
                # game bar events
                # Get escape key press for menu; COPY THIS BLOCK FOR PAUSE MENU
                pause_options = self.__game_skeleton.events(event)
                if pause_options == 0:
                    self.__running = False
                    return True
                elif pause_options == 1:
                    self.__running = False

                # Hit quit
                if event.type == pygame.QUIT:
                    self.__running = False
                # Space bar to set the bool to true to reset
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    restart = False
                    rand = None
                    count = 0
                # Check for cup one click
                elif cup_one.collidepoint(mouse_pos) & on_click1 == CLICKED and restart is False:
                    rand = randint(RAND_RANGE_ONE, RAND_RANGE_TWO)
                    restart = True
                    cup_num = 1
                # Check for cup two click
                elif cup_two.collidepoint(mouse_pos) & on_click1 == CLICKED and restart is False:
                    rand = randint(RAND_RANGE_ONE, RAND_RANGE_TWO)
                    restart = True
                    cup_num = 2
                # Check for cup three click
                elif cup_three.collidepoint(mouse_pos) & on_click1 == CLICKED and restart is False:
                    rand = randint(RAND_RANGE_ONE, RAND_RANGE_TWO)
                    restart = True
                    cup_num = 3

                if rand == 1 and count == 0:
                    count = 1
                    self.__score += 1
                    win = self.__font.render("You Win! Score: ", ANTI_ANILIASING, BLUE)
                    score = self.__font.render(str(self.__score), ANTI_ANILIASING, BLUE)
                    self.__screen.blit(win, (cup_one.centerx, cup_one.centery - TEXT_Y, TEXT_SIZE, TEXT_SIZE))
                    self.__screen.blit(score, (cup_one.centerx + SCORE_X, cup_one.centery - TEXT_Y, TEXT_SIZE, TEXT_SIZE))
                    if cup_num == 1:
                        greg_pos = (cup_two.centerx - CUP_TWO_X, self.__screen.get_rect().centery - OUTER_CUPS_Y)
                    if cup_num == 2:
                        greg_pos = (self.__screen.get_rect().centerx - CUP_ONE_X,
                                    self.__screen.get_rect().centery - INNER_CUP_Y)
                    if cup_num == 3:
                        greg_pos = (cup_two.centerx + CUP_THREE_X, self.__screen.get_rect().centery - OUTER_CUPS_Y)
                    self.__screen.blit(greg, greg_pos)
                elif rand is not None and count == 0:
                    count = 1
                    lose = self.__font.render("You Lose :(", ANTI_ANILIASING, BLUE)
                    self.__screen.blit(lose, (cup_one.centerx, cup_one.centery - TEXT_Y, TEXT_SIZE, TEXT_SIZE))

            # Updates the screen
            pygame.display.flip()
