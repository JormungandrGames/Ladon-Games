#!/usr/bin/python

from resolution_settings import *
from menu import *
from cups.Cups import Cups

# SCREEN CONSTANTS
SCREEN_OPTION = 2
FULL_SCREEN = 0
SCREEN_X = 0
SCREEN_Y = 1

# GAME OPTIONS
CUPS = 1


def main():
    arcade_running = True
    game = None

    # includes
    pygame.init()
    pygame.mixer.init()

    # Resolution Menu
    resolution = SettingsMenu()
    settings = resolution.load_menu_objects()

    # Runs the main menu loop until you want to quit the arcade
    while arcade_running:
        # Get screen settings
        if settings[SCREEN_OPTION] == FULL_SCREEN:
            screen = pygame.display.set_mode((settings[SCREEN_X], settings[SCREEN_Y]), pygame.FULLSCREEN)
        else:
            screen = pygame.display.set_mode((settings[SCREEN_X], settings[SCREEN_Y]))

        # Main Menu
        game_selection = Menu(screen, settings)
        game = game_selection.menu_loop()
        if game == 0:
            arcade_running = False

        if game == CUPS:
            game = Cups(screen)
            arcade_running = game.game_loop()

if __name__ == '__main__':
    main()