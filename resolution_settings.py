import pygame
from pygame.locals import *


class SettingsMenu:
    def __init__(self):
        pygame.init()
        self.__resolutions16_10 = ['1280x800', '1440x900', '1680x1050', '1920x1200', '2560x1600']
        self.__resolutions16_9 = ['852x480', '1280x720', '1365x768', '1600, 900', '1920, 1080']
        self.__resolutions4_3 = ['1024, 768', '1152, 864', '1280, 960', '1400, 1050', '1600, 1200']
        self.__resolutions3_2 = ['720, 480', '1152, 768', '1280, 564', '1440, 960', '2880, 1920']

        # Load text to surfaces, then when the user selects a choice, split and convert to int

    def load_menu_objects(self):
        resolution_list = []
        pygame.display.Info()
        font = pygame.font.SysFont("notosans", 24)
        user_resolution = pygame.display.Info().current_w / pygame.display.Info().current_h;

        # Loads screen
        screen = pygame.display.set_mode((500, 600))
        pygame.display.set_caption('16-Bit Arcade')
        icon = pygame.image.load('resources/Images/game_icon.png')
        pygame.display.set_icon(icon)

        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill((100, 100, 100))

        # Get resolution options

        if user_resolution == 16 / 10:
            for i in range(len(self.__resolutions16_10)):
                res_test = font.render(self.__resolutions16_9[i], 1, (20, 20, 20))
                res_pos = res_test.get_rect()
                res_pos.centerx = background.get_rect().centerx
                res_pos.centery += (80 + (i * 50))
                background.blit(res_test, res_pos)
                screen.blit(background, (0, 0))
                pygame.display.flip()

        elif user_resolution == 16 / 9:
            for i in range(len(self.__resolutions16_9)):
                res_test = font.render(self.__resolutions16_9[i], 1, (20, 20, 20))
                res_pos = res_test.get_rect()
                res_pos.centerx = background.get_rect().centerx
                res_pos.centery += (80 + (i * 50))
                background.blit(res_test, res_pos)
                screen.blit(background, (0, 0))
                pygame.display.flip()

        elif user_resolution == 4 / 3:
            for i in range(len(self.__resolutions4_3)):
                res_test = font.render(self.__resolutions4_3[i], 1, (20, 20, 20))
                res_pos = res_test.get_rect()
                res_pos.centerx = background.get_rect().centerx
                res_pos.centery += (80 + (i * 50))
                background.blit(res_test, res_pos)
                screen.blit(background, (0, 0))
                pygame.display.flip()
        elif user_resolution == 3 / 2:
            for i in range(len(self.__resolutions4_3)):
                res_test = font.render(self.__resolutions4_3[i], 1, (20, 20, 20))
                res_pos = res_test.get_rect()
                res_pos.centerx = background.get_rect().centerx
                res_pos.centery += (80 + (i * 50))
                background.blit(res_test, res_pos)
                screen.blit(background, (0, 0))
                pygame.display.flip()
        else:
            print("Unsupported resolution")

        # Accept button
        accept = pygame.image.load("resources/Images/settings_accept.png")
        accept = pygame.transform.scale(accept, (200, 200))
        b_accept_pos = accept.get_rect()
        b_accept_pos.centerx = background.get_rect().centerx
        b_accept_pos.centery = (background.get_rect().height - accept.get_rect().height)

        background.blit(accept, b_accept_pos)

        # Render font

        text = font.render("Game Settings", 1, (20, 20, 20))
        text_pos = text.get_rect()
        text_pos.centerx = background.get_rect().centerx
        text_pos.centery += 20
        background.blit(text, text_pos)

        screen.blit(background, (0, 0))
        pygame.display.flip()

        while True:
            mouse_pos = pygame.mouse.get_pos()
            (on_click1, on_click2, on_click3) = pygame.mouse.get_pressed()

            if b_accept_pos.collidepoint(mouse_pos) & on_click1 == 1:
                return False

            for event in pygame.event.get():
                if event.type == QUIT:
                    return False

            screen.blit(background, (0, 0))
            pygame.display.flip()
