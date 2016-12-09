from game_skeleton import game_skeleton
from menu import *

L_GRID_PRCNT = [0.10, 0.30, 0.60, 0.10, 0.30, 0.60, 0.90, 0.90]
GRID_THICKNESS = 5
TOT_GRID = 4


class TicTacToe(game_skeleton.Game_Skeleton):
    def __init__(self, screen):
        # Loads the music, -1 means loop it forever
        # Music must be initialized before the game skeleton
        self.__music = pygame.mixer.music.load('tic_tac_toe/resources/music/YodaSong.ogg')
        pygame.mixer.music.play(LOOP_MUSIC)

        # Screen surface
        self.__game_skeleton = game_skeleton.Game_Skeleton(screen)
        self.__screen = screen
        self.__screen.get_rect().height = self.__game_skeleton.get_game_height()
        self.__screen_pos = self.__screen.get_rect()

        # Create the start coordinates of the TTT grid
        self.__l_grid_start_coord \
            = [((self.__screen_pos.height * L_GRID_PRCNT[0]), (self.__screen_pos.width * L_GRID_PRCNT[1])),
               ((self.__screen_pos.height * L_GRID_PRCNT[2]), (self.__screen_pos.width * L_GRID_PRCNT[1])),
               ((self.__screen_pos.height * L_GRID_PRCNT[3]), (self.__screen_pos.width * L_GRID_PRCNT[4])),
               ((self.__screen_pos.height * L_GRID_PRCNT[3]), (self.__screen_pos.width * L_GRID_PRCNT[5]))]

        # Create the end coordinates of the TTT grid
        self.__l_grid_end_coord \
            = [((self.__screen_pos.height * L_GRID_PRCNT[0]), (self.__screen_pos.width * L_GRID_PRCNT[6])),
               ((self.__screen_pos.height * L_GRID_PRCNT[2]), (self.__screen_pos.width * L_GRID_PRCNT[6])),
               ((self.__screen_pos.height * L_GRID_PRCNT[7]), (self.__screen_pos.width * L_GRID_PRCNT[4])),
               ((self.__screen_pos.height * L_GRID_PRCNT[7]), (self.__screen_pos.width * L_GRID_PRCNT[5]))]

        # The TTT grid
        #self.__l_grid = []

        self.__running = True

        self.__game_title = "Tic-Tac-Toe"

        self.__score = 0

    def game_loop(self):
        pause_options = None
        self.__running = True

        while self.__running:
            # Clears the screen and fills it with color (black)

            self.__screen.fill(BLACK)

            # Draw the TTT grid
            for i in range(TOT_GRID):
                pygame.draw.line(self.__screen, WHITE, self.__l_grid_start_coord[i],
                                 self.__l_grid_end_coord[i], GRID_THICKNESS)

            # Blits the game bar
            self.__game_skeleton.blit_game_bar(self.__game_title, self.__score)

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

            pygame.display.flip()
