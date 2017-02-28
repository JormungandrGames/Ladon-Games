import pygame
from Snake import player
from Snake import walls
from game_skeleton import game_skeleton

# COLORS CONSTANTS
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
SNAKE_COLOR_H = (255, 0, 0)

# SCREEN, FONT AND MUSIC CONSTANTS
ANTI_ANILIASING = 1
LOOP_MUSIC = -1
SPEED = 5


class Snake:
    def __init__(self, screen):
        # Sounds
        self.__music = pygame.mixer.music.load('Snake/resources/music/snake_music.ogg')

        # Loads the music, -1 means loop it forever
        pygame.mixer.music.play(LOOP_MUSIC)

        # Screen surface
        self.__game_skeleton = game_skeleton.Game_Skeleton(screen)
        self.__screen = screen
        self.__screen.get_rect().height = self.__game_skeleton.get_game_height()

        # Initialize game title and score
        self.__game_title = "Snake"
        self.__score = 0

        # Running game
        self.__running = True

    def game_loop(self):
        # Call pause
        pause_options = None
        self.__running = True

        # Snake Objects
        snake = player.Snake(self.__screen, self.__screen.get_rect().centerx,
                                  self.__screen.get_rect().centery, SNAKE_COLOR_H)
        game_walls = walls.BuildWalls(self.__screen)

        # Game resets, score is reinitialized
        self.__score = 0

        # snake_head.tail()
        k = 1
        # Game Loop
        while self.__running:
            # Clears the screen and fills it with color (black)
            self.__screen.fill(BLACK)
            self.__score = snake.score()

            if self.__score == -1:
                # Snake Objects
                self.__running = False
                Snake.game_loop(self)

            # Blits the game bar
            self.__game_skeleton.blit_game_bar(self.__game_title, self.__score)

            # Blit the Snake and walls
            head_rect = snake.blit()
            walls_rect = game_walls.blit()

            # Gets users buttons events
            snake.direction()

            # Moves the snake; Don't change this speed to move faster
            k += 1
            if k % SPEED == 0:
                snake.move()

            for i in walls_rect:
                if i.colliderect(head_rect):
                    snake.kill_snake()
                    self.__score = -1

            # On mouse and keyboard events
            for event in pygame.event.get():
                # Hit quit
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

            # Updates the screen
            pygame.display.update()
