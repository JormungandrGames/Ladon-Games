from __future__ import division

from game_skeleton.pause_menu import *
from pong import controls
from pong import pong_game

# Pong game!
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
MAIN_MENU = 1
EXIT = 2
MENU = 0


class PongMenu:
    def __init__(self, screen):
        # variables
        self.__clock = pygame.time.Clock()
        self.__fps = 60
        self.__alpha = 0
        self.__l_blit_object = []
        # Screen surface
        self.__screen = screen
        # Running game
        self.__running = True

        # Init Music
        self.__music = pygame.mixer.music.load('pong/resources/music/pong_music.ogg')

        # Load Font
        self.__font = pygame.font.Font('pong/resources/fonts/NIAGENG.TTF', 100)

        # Constructor Call
        self.__constructor()

    def __constructor(self):
        # Loads the music, -1 means loop it forever
        # pygame.mixer.music.play(-1)

        # Load Buttons and title
        # title
        self.__f_game_title = self.__font.render("ULTIMATE PONG", 1, WHITE)
        self.__l_blit_object.append(self.__f_game_title)
        self.__f_game_title_pos = self.__f_game_title.get_rect()
        self.__f_game_title_pos.centerx = self.__screen.get_rect().centerx
        self.__f_game_title_pos.centery = self.__screen.get_rect().top + 100
        self.__l_blit_object.append(self.__f_game_title_pos)
        # play button
        self.__i_play_button = pygame.image.load("pong/resources/images/background.png").convert_alpha()
        self.__i_play_button = pygame.transform.scale(self.__i_play_button, (200, 200))
        self.__l_blit_object.append(self.__i_play_button)
        self.__i_play_button_pos = self.__i_play_button.get_rect()
        self.__i_play_button_pos.centerx = self.__screen.get_rect().centerx
        self.__i_play_button_pos.centery = self.__screen.get_rect().top + 325
        self.__l_blit_object.append(self.__i_play_button_pos)
        # menu button
        self.__i_menu_button = pygame.image.load("pong/resources/images/background.png").convert_alpha()
        self.__i_menu_button = pygame.transform.scale(self.__i_menu_button, (200, 200))
        self.__l_blit_object.append(self.__i_menu_button)
        self.__i_menu_button_pos = self.__i_menu_button.get_rect()
        self.__i_menu_button_pos.centerx = self.__screen.get_rect().centerx - 250
        self.__i_menu_button_pos.centery = self.__screen.get_rect().top + 500
        self.__l_blit_object.append(self.__i_menu_button_pos)
        # controls button
        self.__i_help_button = pygame.image.load("pong/resources/images/background.png").convert_alpha()
        self.__i_help_button = pygame.transform.scale(self.__i_help_button, (200, 200))
        self.__l_blit_object.append(self.__i_help_button)
        self.__i_help_button_pos = self.__i_help_button.get_rect()
        self.__i_help_button_pos.centerx = self.__screen.get_rect().centerx
        self.__i_help_button_pos.centery = self.__screen.get_rect().top + 550
        self.__l_blit_object.append(self.__i_help_button_pos)
        # exit button
        self.__i_exit_button = pygame.image.load("pong/resources/images/background.png").convert_alpha()
        self.__i_exit_button = pygame.transform.scale(self.__i_exit_button, (200, 200))
        self.__l_blit_object.append(self.__i_exit_button)
        self.__i_exit_button_pos = self.__i_exit_button.get_rect()
        self.__i_exit_button_pos.centerx = self.__screen.get_rect().centerx + 250
        self.__i_exit_button_pos.centery = self.__screen.get_rect().top + 500
        self.__l_blit_object.append(self.__i_exit_button_pos)
        # play string
        self.__f_play_button = self.__font.render("PLAY", 1, WHITE)
        self.__f_play_button = pygame.transform.scale(self.__f_play_button, (150, 100))
        self.__l_blit_object.append(self.__f_play_button)
        self.__f_play_button_pos = self.__f_play_button.get_rect()
        self.__f_play_button_pos.centerx = self.__screen.get_rect().centerx
        self.__f_play_button_pos.centery = self.__screen.get_rect().top + 325
        self.__l_blit_object.append(self.__f_play_button_pos)
        # menu string
        self.__f_menu_button = self.__font.render("MENU", 1, WHITE)
        self.__f_menu_button = pygame.transform.scale(self.__f_menu_button, (150, 100))
        self.__l_blit_object.append(self.__f_menu_button)
        self.__f_menu_button_pos = self.__f_menu_button.get_rect()
        self.__f_menu_button_pos.centerx = self.__screen.get_rect().centerx - 250
        self.__f_menu_button_pos.centery = self.__screen.get_rect().top + 500
        self.__l_blit_object.append(self.__f_menu_button_pos)
        # exit string
        self.__f_exit_button = self.__font.render("EXIT", 1, WHITE)
        self.__f_exit_button = pygame.transform.scale(self.__f_exit_button, (150, 100))
        self.__l_blit_object.append(self.__f_exit_button)
        self.__f_exit_button_pos = self.__f_exit_button.get_rect()
        self.__f_exit_button_pos.centerx = self.__screen.get_rect().centerx + 250
        self.__f_exit_button_pos.centery = self.__screen.get_rect().top + 500
        self.__l_blit_object.append(self.__f_exit_button_pos)
        # controls string
        self.__f_help_button = self.__font.render("HELP", 1, WHITE)
        self.__f_help_button = pygame.transform.scale(self.__f_help_button, (150, 100))
        self.__l_blit_object.append(self.__f_help_button)
        self.__f_help_button_pos = self.__f_help_button.get_rect()
        self.__f_help_button_pos.centerx = self.__screen.get_rect().centerx
        self.__f_help_button_pos.centery = self.__screen.get_rect().top + 550
        self.__l_blit_object.append(self.__f_help_button_pos)

    def game_loop(self):
        game_start = True

        # Call pause
        pause = Pause(self.__screen)
        c_controls = controls.Controls(self.__screen)
        pause_options = None
        self.__running = True

        while self.__running:
            # Check for events
            mouse_pos = pygame.mouse.get_pos()
            (on_click1, on_click2, on_click3) = pygame.mouse.get_pressed()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.__running = False

                elif self.__i_play_button_pos.collidepoint(mouse_pos) & on_click1 == 1 and game_start:
                    self.__running = False
                    ponggame = pong_game.PongGame(self.__screen)
                    arcade_running = ponggame.game_loop()
                    if arcade_running != MENU:
                        return arcade_running
                    if arcade_running == MENU:
                        self.__running = True

                elif self.__i_menu_button_pos.collidepoint(mouse_pos) & on_click1 == 1 and game_start:
                    self.__running = False
                    return True

                elif self.__i_help_button_pos.collidepoint(mouse_pos) & on_click1 == 1 and game_start:
                    control_screen = c_controls.control_loop()
                    if control_screen == EXIT:
                        self.__running = False
                        return

                # Get escape key press for menu; COPY THIS BLOCK FOR PAUSE MENU
                elif pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    pause_options = pause.pause_loop()
                    if pause_options == 0:
                        self.__running = False
                        return True
                    elif pause_options == 1:
                        self.__running = False

                elif self.__i_exit_button_pos.collidepoint(mouse_pos) & on_click1 == 1 and game_start:
                    self.__running = False

            # Blit
            self.__screen.fill(BLACK)
            for i in range(len(self.__l_blit_object)):
                if i % 2 == 0:
                    rect = i + 1
                    self.__screen.blit(self.__l_blit_object[i], self.__l_blit_object[rect])

            pygame.display.flip()

            # Clock
            self.__clock.tick(self.__fps)
            self.__clock.tick_busy_loop()
