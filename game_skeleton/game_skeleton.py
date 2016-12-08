import pygame

from game_skeleton import pause_menu
from game_skeleton import game_bar


class Game_Skeleton(game_bar.Game_Bar, pause_menu.Pause):
    def __init__(self, screen):
        self.__screen = screen
        self.__game_title = " "
        self.__game_score = 0

        # Create the game bar and change the game screen based on it
        self.__game_bar = game_bar.Game_Bar(self.__screen, self.__game_title, self.__game_score)
        game_bar_height = self.__game_bar.get_game_bar_height()
        self.__height = screen.get_rect().height - game_bar_height

        self.__pause_menu = pause_menu.Pause(screen)

        self.__pause_options = None

    def get_game_height(self):
        return self.__height

    def blit_game_bar(self, game_title, game_score='N/A'):
        self.__game_title = game_title
        self.__game_score = game_score
        self.__game_bar.blit_game_bar(self.__game_title, self.__game_score)

    def events(self, event, game_music_running=False, game_sound_running=False):
        self.__game_bar.events(event)

        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            self.__pause_options = self.__pause_menu.pause_loop()

        return self.__pause_options
