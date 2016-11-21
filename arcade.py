#!/usr/bin/python

from resolution_settings import *
from menu import *
from cups.Cups import Cups

FULL_SCREEN = 0
SCREEN_X = 0
SCREEN_Y = 1
SCREEN_OPTION = 2


def main():
    # includes
    pygame.init()
    pygame.mixer.init()

    # Resolution Menu
    resolution = SettingsMenu()
    settings = resolution.load_menu_objects()

    # Get screen settings
    if settings[SCREEN_OPTION] == FULL_SCREEN:
        screen = pygame.display.set_mode((settings[SCREEN_X], settings[SCREEN_Y]), pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode((settings[SCREEN_X], settings[SCREEN_Y]))

    # Main Menu
    game_selection = Menu(screen, settings)
    game = game_selection.menu_loop()
    pygame.event.clear()
    if game == 1:
        game = Cups(screen)
        game.game_loop()

if __name__ == '__main__':
    main()
