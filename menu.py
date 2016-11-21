#!/usr/bin/python

import pygame
import time

FADE_IN = 0
FADE_IN_TIME = 3
FADE_OUT_TIME = 3
FADE_IN_EASING = lambda x: x
FADE_OUT_EASING = lambda x: x
BLACK = (0, 0, 0)
WHITE = (250, 250, 250)

QUIT = 0
CUPS = 1


class Menu:
    def __init__(self, screen, settings):
        self.__settings = settings
        self.__screen = screen
        self.__l_blit_object = []
        self.__clock = pygame.time.Clock()
        self.__fps = 60
        self.__alpha = 0

        # Running loop
        self.__running = True

        # Fonts
        self.__font = pygame.font.Font('resources/fonts/SkyrimFont.ttf', int(settings[0]/30))

        # Images

        # Music
        self.__music = pygame.mixer.music.load('resources/music/Star_Fox_Space_Armada.mp3')

        # Sounds
        self.__selection = pygame.mixer.Sound('resources/sounds/DarkSoulsStartSound.wav')

        # Constructor Call
        self.__constructor()

    def __constructor(self):

        # Loads the icon and surface name
        icon = pygame.image.load('resources/images/game_icon.png').convert_alpha()
        pygame.display.set_caption('16-Bit Hero Arcade')
        pygame.display.set_icon(icon)

        if self.__settings[2] == 0:
            self.__fade_surface = pygame.surface.Surface((self.__settings[0], self.__settings[1]), pygame.FULLSCREEN)
        else:
            self.__fade_surface = pygame.surface.Surface((self.__settings[0], self.__settings[1]))

        # Music
        pygame.mixer.music.play(-1)
        # Title set up
        self.__f_game_title = self.__font.render("16-Bit-Hero-Arcade", 1, WHITE)
        self.__l_blit_object.append(self.__f_game_title)
        self.__f_game_title_pos = self.__f_game_title.get_rect()
        self.__f_game_title_pos.centerx = self.__screen.get_rect().centerx
        self.__f_game_title_pos.centery = self.__screen.get_rect().top + 100
        self.__l_blit_object.append(self.__f_game_title_pos)
        # Quit font set up
        self.__f_game_quit = self.__font.render("Quit", 1, WHITE)
        self.__l_blit_object.append(self.__f_game_quit)
        self.__f_game_quit_pos = self.__f_game_quit.get_rect()
        self.__f_game_quit_pos.centerx = self.__screen.get_rect().centerx
        self.__f_game_quit_pos.centery = self.__screen.get_rect().bottom - 100
        self.__l_blit_object.append(self.__f_game_quit_pos)
        # Cups temp setup
        self.__f_cups = self.__font.render("Cups", 1, WHITE)
        self.__l_blit_object.append(self.__f_cups)
        self.__f_cups_pos = self.__f_cups.get_rect()
        self.__f_cups_pos.centerx = self.__screen.get_rect().centerx
        self.__f_cups_pos.centery = self.__screen.get_rect().centery - 200
        self.__l_blit_object.append(self.__f_cups_pos)
        # Pacman Button

    def menu_loop(self):
        state_change = time.time()
        game_start = True

        while self.__running:
            # Check for events
            mouse_pos = pygame.mouse.get_pos()
            (on_click1, on_click2, on_click3) = pygame.mouse.get_pressed()

            event = pygame.event.peek()
            if event.type == pygame.QUIT and game_start:
                pygame.mixer.music.fadeout(3000)
                self.__selection.play()
                self.__running = False
                return

            elif self.__f_cups_pos.collidepoint(mouse_pos) & on_click1 == 1:
                return CUPS

            elif self.__f_game_quit_pos.collidepoint(mouse_pos) & on_click1 == 1 and game_start:
                pygame.mixer.music.fadeout(3000)
                self.__selection.play()
                game_start = False

            # Fade In
            if game_start:
                state_time_in = time.time() - state_change
                if int(self.__alpha) == 0:
                    self.__alpha = FADE_IN_EASING(1.0 * state_time_in / FADE_IN_TIME)
                    self.__fade_surface.set_alpha(255 * self.__alpha)
            else:
                state_time_out = time.time() - state_change - state_time_in
                self.__alpha = 1. - FADE_OUT_EASING(1.0 * state_time_out / FADE_OUT_TIME)
                self.__fade_surface.set_alpha(255 * self.__alpha)
                if (self.__alpha * 255) < 0:
                    self.__running = False

            # Blit
            self.__screen.fill(BLACK)
            self.__fade_surface.fill(BLACK)
            for i in range(len(self.__l_blit_object)):
                if i % 2 == 0:
                    rect = i + 1
                    self.__fade_surface.blit(self.__l_blit_object[i], self.__l_blit_object[rect])

            self.__fade_surface.blit(self.__fade_surface, (0, 0))
            self.__screen.blit(self.__fade_surface, self.__screen.get_rect())
            pygame.display.flip()

            # Clock
            self.__clock.tick(self.__fps)
            self.__clock.tick_busy_loop()
