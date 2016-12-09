#!/usr/bin/python

import pygame
import time

#
# CHECK LINE 127 FOR ADDING GAMES
#

# ALPHA FADING CONSTANTS
FADE_OUT_EASING = lambda x: x
FADE_IN_EASING = lambda x: x
ALPHA_MULTIPLER = 1.0
ANTI_ANILIASING = 1
FADE_OUT_TIME = 1.5
FADE_IN_TIME = 3
MAX_ALPHA = 255
MIN_ALPHA = 0
FADE_IN = 0

# COLORS CONSTANTS
WHITE = (250, 250, 250)
BLACK = (0, 0, 0)

# LOCATIONS CONSTANTS
FADE_BLIT = (0, 0)
TITLE_Y = 100
QUIT_Y = 100
ROW_ONE = 200
ROW_TWO = 300
CUPS_Y = 450
PONG_Y = 300
SNAKE_Y = 300
PONG_X = 100
SNAKE_X = 100
QUIT = 0

# GAMES
CUPS = 1
PONG = 2
SNAKE = 3


# SCREEN CONSTANTS AND MUSIC
MAX_SCREEN_SETTINGS = 2
FONT_MODIFIER = 30
MUSIC_FADE = 3000
LOOP_MUSIC = -1
SCREEN_X = 0
SCREEN_Y = 1
CLICKED = 1


class Menu:
    def __init__(self, screen, settings):
        # Sets up the screen variables
        self.__settings = settings
        self.__screen = screen

        # List of blit objects
        self.__l_blit_object = []

        # Start alpha
        self.__alpha = 0

        # Running loop
        self.__running = True

        # Fonts
        self.__font = pygame.font.Font('resources/fonts/SkyrimFont.ttf', int(settings[SCREEN_X]/FONT_MODIFIER))

        # Music
        self.__music = pygame.mixer.music.load('resources/music/Star_Fox_Space_Armada.ogg')

        # Sounds
        self.__selection = pygame.mixer.Sound('resources/sounds/DarkSoulsStartSound.wav')

        # Constructor Call
        self.__constructor()

    def __constructor(self):
        # Loads the icon and surface name
        icon = pygame.image.load('resources/images/game_icon.png').convert_alpha()
        pygame.display.set_caption('16-Bit Hero Arcade')
        pygame.display.set_icon(icon)

        # Sets screen size if it's full screen or not
        if self.__settings[MAX_SCREEN_SETTINGS] == 0:
            self.__fade_surface = pygame.surface.Surface((self.__settings[SCREEN_X], self.__settings[SCREEN_Y]), pygame.FULLSCREEN)
        else:
            self.__fade_surface = pygame.surface.Surface((self.__settings[SCREEN_X], self.__settings[SCREEN_Y]))

        # Music
        pygame.mixer.music.play(LOOP_MUSIC)

        # Title set up
        self.__f_game_title = self.__font.render("16-Bit-Hero-Arcade", ANTI_ANILIASING, WHITE)
        self.__l_blit_object.append(self.__f_game_title)
        self.__f_game_title_pos = self.__f_game_title.get_rect()
        self.__f_game_title_pos.centerx = self.__screen.get_rect().centerx
        self.__f_game_title_pos.centery = self.__screen.get_rect().top + TITLE_Y
        self.__l_blit_object.append(self.__f_game_title_pos)

        # Image cups set up
        self.__i_cups_button = pygame.image.load("cups/resources/images/cups_menu.png").convert_alpha()
        self.__i_cups_button = pygame.transform.scale(self.__i_cups_button, (150, 150))
        self.__l_blit_object.append(self.__i_cups_button)
        self.__i_cups_button_pos = self.__i_cups_button.get_rect()
        self.__i_cups_button_pos.centerx = self.__screen.get_rect().centerx
        self.__i_cups_button_pos.centery = self.__screen.get_rect().top + CUPS_Y
        self.__l_blit_object.append(self.__i_cups_button_pos)

        # Image pong set up
        self.__i_pong_button = pygame.image.load("pong/resources/images/pong_menu.png").convert_alpha()
        self.__i_pong_button = pygame.transform.scale(self.__i_pong_button, (200, 225))
        self.__l_blit_object.append(self.__i_pong_button)
        self.__i_pong_button_pos = self.__i_pong_button.get_rect()
        self.__i_pong_button_pos.centerx = self.__screen.get_rect().centerx + PONG_X
        self.__i_pong_button_pos.centery = self.__screen.get_rect().top + PONG_Y
        self.__l_blit_object.append(self.__i_pong_button_pos)

        # Image snake set up
        self.__i_snake_button = pygame.image.load("Snake/resources/images/snake_menu.png").convert_alpha()
        self.__i_snake_button = pygame.transform.scale(self.__i_snake_button, (225, 225))
        self.__l_blit_object.append(self.__i_snake_button)
        self.__i_snake_button_pos = self.__i_snake_button.get_rect()
        self.__i_snake_button_pos.centerx = self.__screen.get_rect().centerx - SNAKE_X
        self.__i_snake_button_pos.centery = self.__screen.get_rect().top + SNAKE_Y
        self.__l_blit_object.append(self.__i_snake_button_pos)

        # Quit font set up
        self.__f_game_quit = self.__font.render("Quit", ANTI_ANILIASING, WHITE)
        self.__l_blit_object.append(self.__f_game_quit)
        self.__f_game_quit_pos = self.__f_game_quit.get_rect()
        self.__f_game_quit_pos.centerx = self.__screen.get_rect().centerx
        self.__f_game_quit_pos.centery = self.__screen.get_rect().bottom - QUIT_Y
        self.__l_blit_object.append(self.__f_game_quit_pos)

        # Cups temp setup
        self.__f_cups = self.__font.render("Cups", ANTI_ANILIASING, WHITE)
        self.__l_blit_object.append(self.__f_cups)
        self.__f_cups_pos = self.__f_cups.get_rect()
        self.__f_cups_pos.centerx = self.__screen.get_rect().centerx
        self.__f_cups_pos.centery = self.__screen.get_rect().top + CUPS_Y
        self.__l_blit_object.append(self.__f_cups_pos)

        # Pong temp setup
        self.__f_pong = self.__font.render("Pong", ANTI_ANILIASING, WHITE)
        self.__l_blit_object.append(self.__f_pong)
        self.__f_pong_pos = self.__f_pong.get_rect()
        self.__f_pong_pos.centerx = self.__screen.get_rect().centerx + PONG_X
        self.__f_pong_pos.centery = self.__screen.get_rect().top + PONG_Y
        self.__l_blit_object.append(self.__f_pong_pos)

        # Snake temp setup
        self.__f_Snake = self.__font.render("Snake", ANTI_ANILIASING, WHITE)
        self.__l_blit_object.append(self.__f_Snake)
        self.__f_Snake_pos = self.__f_Snake.get_rect()
        self.__f_Snake_pos.centerx = self.__screen.get_rect().centerx - SNAKE_X
        self.__f_Snake_pos.centery = self.__screen.get_rect().top + SNAKE_Y
        self.__l_blit_object.append(self.__f_Snake_pos)

    def menu_loop(self):
        # Set up variables
        state_change = time.time()
        game_start = True
        game_num = None

        while self.__running:
            # Check for mouse clicks
            mouse_pos = pygame.mouse.get_pos()
            (on_click1, on_click2, on_click3) = pygame.mouse.get_pressed()

            # Peek for queued events
            event = pygame.event.peek()
            if event.type == pygame.QUIT and game_start:
                pygame.mixer.music.fadeout(MUSIC_FADE)
                self.__selection.play()
                self.__running = False
                return
            # Returns the cups index number. ADD GAMES AFTER HERE AND CONSTANT AT TOP
            elif self.__f_cups_pos.collidepoint(mouse_pos) and on_click1 == CLICKED and game_start:
                pygame.mixer.music.fadeout(MUSIC_FADE)
                self.__selection.play()
                game_start = False
                game_num = CUPS

            # Returns the pong index number
            elif self.__f_pong_pos.collidepoint(mouse_pos) and on_click1 == CLICKED and game_start:
                pygame.mixer.music.fadeout(MUSIC_FADE)
                self.__selection.play()
                game_start = False
                game_num = PONG

            # Returns the snake index number
            elif self.__f_Snake_pos.collidepoint(mouse_pos) and on_click1 == CLICKED and game_start:
                pygame.mixer.music.fadeout(MUSIC_FADE)
                self.__selection.play()
                game_start = False
                game_num = SNAKE
            # Quits the arcade
            elif self.__f_game_quit_pos.collidepoint(mouse_pos) and on_click1 == CLICKED and game_start:
                return QUIT

            # Fade In magic starts here
            if game_start:
                state_time_in = time.time() - state_change
                if int(self.__alpha) == MIN_ALPHA:
                    self.__alpha = FADE_IN_EASING(ALPHA_MULTIPLER * state_time_in / FADE_IN_TIME)
                    self.__fade_surface.set_alpha(MAX_ALPHA * self.__alpha)
            # Fade out magic starts here
            else:
                state_time_out = time.time() - state_change - state_time_in
                self.__alpha = 1. - FADE_OUT_EASING(ALPHA_MULTIPLER * state_time_out / FADE_OUT_TIME)
                self.__fade_surface.set_alpha(MAX_ALPHA * self.__alpha)
                if (self.__alpha * MAX_ALPHA) < MIN_ALPHA:
                    self.__running = False
                    return game_num

            # Fill the screen and blit all of the buttons
            self.__screen.fill(BLACK)
            self.__fade_surface.fill(BLACK)
            for i in range(len(self.__l_blit_object)):
                if i % 2 == 0:
                    rect = i + 1
                    self.__fade_surface.blit(self.__l_blit_object[i], self.__l_blit_object[rect])

            # Blits the faded surface
            self.__fade_surface.blit(self.__fade_surface, FADE_BLIT)
            self.__screen.blit(self.__fade_surface, self.__screen.get_rect())
            pygame.display.flip()
