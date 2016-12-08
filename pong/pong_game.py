from __future__ import division

import pygame
from game_skeleton import game_skeleton
from pong import pong_resources
from pong import winner_display

WHITE = (200, 200, 200)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
PADDLE_SHORT = 20
PADDLE_LONG = 165
RADIUS = 15
FILL = 0
SCREEN_BUFFER = 75
PLAYER_ONE = 0
PLAYER_TWO = 1
MENU = 0


class PongGame:
    def __init__(self, screen):
        # Loads the music, -1 means loop it forever
        self.__music = pygame.mixer.music.load('pong/resources/music/NotTheFuture.ogg')
        pygame.mixer.music.play(-1)
        # variables
        self.__game_title = "Pong"
        self.__clock = pygame.time.Clock()
        self.__fps = 60
        self.__alpha = 0
        self.__l_blit_object = []
        self.__l_blit_score_one = []
        self.__l_blit_score_two = []
        # Screen surface
        self.__game_skeleton = game_skeleton.Game_Skeleton(screen)
        self.__screen = screen
        self.__screen.get_rect().height = self.__game_skeleton.get_game_height()
        # Running game
        self.__running = True

        # Load Font
        self.__font = pygame.font.Font('pong/resources/fonts/NIAGENG.TTF', 100)

        # Constructor Call
        self.__constructor()

    def __constructor(self):
        # Load title
        # title
        self.__f_game_title = self.__font.render("ULTIMATE PONG", 1, WHITE)
        self.__l_blit_object.append(self.__f_game_title)
        self.__f_game_title_pos = self.__f_game_title.get_rect()
        self.__f_game_title_pos.centerx = self.__screen.get_rect().centerx
        self.__f_game_title_pos.centery = self.__screen.get_rect().top + 100
        self.__l_blit_object.append(self.__f_game_title_pos)

        # score player one
        self.__f_player_one_s0 = self.__font.render("Player 1: 0", 1, WHITE)
        self.__l_blit_score_one.append(self.__f_player_one_s0)
        self.__f_player_one_s0_pos = self.__f_player_one_s0.get_rect()
        self.__f_player_one_s0_pos.bottomleft = self.__screen.get_rect().bottomleft
        self.__l_blit_score_one.append(self.__f_player_one_s0_pos)

        self.__f_player_one_s1 = self.__font.render("Player 1: 1", 1, WHITE)
        self.__l_blit_score_one.append(self.__f_player_one_s1)
        self.__f_player_one_s1_pos = self.__f_player_one_s1.get_rect()
        self.__f_player_one_s1_pos.bottomleft = self.__screen.get_rect().bottomleft
        self.__l_blit_score_one.append(self.__f_player_one_s1_pos)

        self.__f_player_one_s2 = self.__font.render("Player 1: 2", 1, WHITE)
        self.__l_blit_score_one.append(self.__f_player_one_s2)
        self.__f_player_one_s2_pos = self.__f_player_one_s2.get_rect()
        self.__f_player_one_s2_pos.bottomleft = self.__screen.get_rect().bottomleft
        self.__l_blit_score_one.append(self.__f_player_one_s2_pos)

        self.__f_player_one_s3 = self.__font.render("Player 1: 3", 1, WHITE)
        self.__l_blit_score_one.append(self.__f_player_one_s3)
        self.__f_player_one_s3_pos = self.__f_player_one_s3.get_rect()
        self.__f_player_one_s3_pos.bottomleft = self.__screen.get_rect().bottomleft
        self.__l_blit_score_one.append(self.__f_player_one_s3_pos)

        self.__f_player_one_s4 = self.__font.render("Player 1: 4", 1, WHITE)
        self.__l_blit_score_one.append(self.__f_player_one_s4)
        self.__f_player_one_s4_pos = self.__f_player_one_s4.get_rect()
        self.__f_player_one_s4_pos.bottomleft = self.__screen.get_rect().bottomleft
        self.__l_blit_score_one.append(self.__f_player_one_s4_pos)

        self.__f_player_one_s5 = self.__font.render("Player 1: 5", 1, WHITE)
        self.__l_blit_score_one.append(self.__f_player_one_s5)
        self.__f_player_one_s5_pos = self.__f_player_one_s5.get_rect()
        self.__f_player_one_s5_pos.bottomleft = self.__screen.get_rect().bottomleft
        self.__l_blit_score_one.append(self.__f_player_one_s5_pos)

        # score player 2
        self.__f_player_two_s0 = self.__font.render("Player 2: 0", 1, WHITE)
        self.__l_blit_score_two.append(self.__f_player_two_s0)
        self.__f_player_two_s0_pos = self.__f_player_two_s0.get_rect()
        self.__f_player_two_s0_pos.bottomright = self.__screen.get_rect().bottomright
        self.__l_blit_score_two.append(self.__f_player_two_s0_pos)

        self.__f_player_two_s1 = self.__font.render("Player 2: 1", 1, WHITE)
        self.__l_blit_score_two.append(self.__f_player_two_s1)
        self.__f_player_two_s1_pos = self.__f_player_two_s1.get_rect()
        self.__f_player_two_s1_pos.bottomright = self.__screen.get_rect().bottomright
        self.__l_blit_score_two.append(self.__f_player_two_s1_pos)

        self.__f_player_two_s2 = self.__font.render("Player 2: 2", 1, WHITE)
        self.__l_blit_score_two.append(self.__f_player_two_s2)
        self.__f_player_two_s2_pos = self.__f_player_two_s2.get_rect()
        self.__f_player_two_s2_pos.bottomright = self.__screen.get_rect().bottomright
        self.__l_blit_score_two.append(self.__f_player_two_s2_pos)

        self.__f_player_two_s3 = self.__font.render("Player 2: 3", 1, WHITE)
        self.__l_blit_score_two.append(self.__f_player_two_s3)
        self.__f_player_two_s3_pos = self.__f_player_two_s3.get_rect()
        self.__f_player_two_s3_pos.bottomright = self.__screen.get_rect().bottomright
        self.__l_blit_score_two.append(self.__f_player_two_s3_pos)

        self.__f_player_two_s4 = self.__font.render("Player 2: 4", 1, WHITE)
        self.__l_blit_score_two.append(self.__f_player_two_s4)
        self.__f_player_two_s4_pos = self.__f_player_two_s4.get_rect()
        self.__f_player_two_s4_pos.bottomright = self.__screen.get_rect().bottomright
        self.__l_blit_score_two.append(self.__f_player_two_s4_pos)

        self.__f_player_two_s5 = self.__font.render("Player 2: 5", 1, WHITE)
        self.__l_blit_score_two.append(self.__f_player_two_s5)
        self.__f_player_two_s5_pos = self.__f_player_two_s5.get_rect()
        self.__f_player_two_s5_pos.bottomright = self.__screen.get_rect().bottomright
        self.__l_blit_score_two.append(self.__f_player_two_s5_pos)

    def game_loop(self):

        player_one = self.__screen.get_rect().left + (SCREEN_BUFFER + PADDLE_SHORT)
        player_two = self.__screen.get_rect().right - SCREEN_BUFFER
        pong_ball = pong_resources.PongBall(self.__screen)
        paddle_one = pong_resources.Paddle(self.__screen, RED, player_one)
        paddle_two = pong_resources.Paddle(self.__screen, BLUE, player_two)
        k = 0
        j = 0

        winnner_display = winner_display.WinnerDisplay(self.__screen)

        while self.__running:
            self.__screen.fill(BLACK)
            # Get mouse clicks
            mouse_pos = pygame.mouse.get_pos()
            (on_click1, on_click2, on_click3) = pygame.mouse.get_pressed()

            # Blits the game bar
            self.__game_skeleton.blit_game_bar(self.__game_title)

            paddle_one.display_paddle()
            paddle_two.display_paddle()
            pong_ball.display_pong_ball()
            score = pong_ball.update_pong_ball(paddle_one, paddle_two)
            if score == PLAYER_ONE:
                k += 2
            if score == PLAYER_TWO:
                j += 2

            if k == 10 or j == 10:
                if k > j:
                    display_option = winnner_display.pause_loop(PLAYER_ONE)
                if j > k:
                    display_option = winnner_display.pause_loop(PLAYER_TWO)

                if display_option == 0:
                    self.__running = False
                if display_option == 1:
                    k = 0
                    j = 0
                if display_option == 2:
                    self.__running = False
                    return True
                if display_option == 3:
                    self.__running = False
                    return MENU

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.__running = False

                # Check for Pause menu events, and
                # game bar events
                # Get escape key press for menu; COPY THIS BLOCK FOR PAUSE MENU
                pause_options = self.__game_skeleton.events(event)
                if pause_options == 0:
                    self.__running = False
                    return True
                elif pause_options == 1:
                    self.__running = False

            if pygame.key.get_pressed()[pygame.K_o] != 0:
                paddle_two.up_paddle()

            if pygame.key.get_pressed()[pygame.K_l] != 0:
                paddle_two.down_paddle()

            if pygame.key.get_pressed()[pygame.K_w] != 0:
                paddle_one.up_paddle()

            if pygame.key.get_pressed()[pygame.K_s] != 0:
                paddle_one.down_paddle()


            # Blit
            for i in range(len(self.__l_blit_object)):
                if i % 2 == 0:
                    rect = i + 1
                    self.__screen.blit(self.__l_blit_object[i], self.__l_blit_object[rect])

            self.__screen.blit(self.__l_blit_score_one[k], self.__l_blit_score_one[k+1])
            self.__screen.blit(self.__l_blit_score_two[j], self.__l_blit_score_two[j + 1])
            pygame.display.flip()

            # Clock
            self.__clock.tick(self.__fps)
            self.__clock.tick_busy_loop()
