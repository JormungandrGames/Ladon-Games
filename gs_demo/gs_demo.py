from game_skeleton import game_skeleton
from menu import *


class GameSkeletonDemo(game_skeleton.Game_Skeleton):
    def __init__(self, screen):
        # Loads the music, -1 means loop it forever
        # Music must be initialized before the game skeleton
        self.__music = pygame.mixer.Sound('gs_demo/resources/music/YodaSong.ogg')
        pygame.mixer.music.play(LOOP_MUSIC)

        # Screen surface
        self.__screen = screen
        self.__game_skeleton = game_skeleton.Game_Skeleton(self.__screen)
        self.__screen.get_rect().height = self.__game_skeleton.get_game_height()
        self.__screen_pos = self.__screen.get_rect()

        self.__running = True

        self.__game_title = "Game Skeleton Demo"

    def game_loop(self):
        pause_options = None
        self.__running = True

        while self.__running:
            # Clears the screen and fills it with color (black)

            self.__screen.fill(BLACK)

            # Blits the game bar
            self.__game_skeleton.blit_game_bar(self.__game_title)

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
