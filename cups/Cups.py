import pygame
from random import randint

# Cup game!
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)


class Cups:
    def __init__(self, screen):
        # Screen surface
        self.__screen = screen

        # Running game
        self.__running = True

        # Init Music
        self.__music = pygame.mixer.music.load('cups/resources/music/YodaSong.mp3')

        # Red exit button
        self.__exit = pygame.image.load('cups/resources/images/exit.png').convert_alpha()
        self.__exit = pygame.transform.scale(self.__exit, (40, 40))

        # Load Font
        self.__font = pygame.font.Font('cups/resources/fonts/NIAGENG.TTF', 100)

    def game_loop(self):
        # Loads the music, -1 means loop it forever
        pygame.mixer.music.play(-1)

        # Reload the cups and font
        restart = False

        rand = None

        # Game Loop
        while self.__running:
            # Clears the screen and fills it with color (black)
            if restart is False:
                self.__screen.fill(BLACK)

            # Load the exit button
            self.__screen.blit(self.__exit, (0, 0, 0, 0))

            # Load the cups
            cup_two = pygame.draw.rect(self.__screen, RED, (self.__screen.get_rect().centerx - 100,
                                                            (self.__screen.get_rect().centery - 50), 200, 300), 1)
            cup_one = pygame.draw.rect(self.__screen, RED, (cup_two.centerx - 400,
                                                            (self.__screen.get_rect().centery - 200), 200, 300), 1)
            cup_three = pygame.draw.rect(self.__screen, RED, (cup_two.centerx + 200,
                                                              self.__screen.get_rect().centery - 200, 200, 300), 1)

            # Get mouse clicks
            mouse_pos = pygame.mouse.get_pos()
            (on_click1, on_click2, on_click3) = pygame.mouse.get_pressed()

            # On mouse and keyboard events
            for event in pygame.event.get():
                # Hit quit
                if event.type == pygame.QUIT:
                    self.__running = False
                # Space bar to set the bool to true to reset
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    restart = False
                    rand = None

                elif cup_one.collidepoint(mouse_pos) & on_click1 == 1 and restart is False:
                    rand = randint(1, 3)
                    restart = True

                elif cup_two.collidepoint(mouse_pos) & on_click1 == 1 and restart is False:
                    rand = randint(1, 3)
                    restart = True

                elif cup_three.collidepoint(mouse_pos) & on_click1 == 1 and restart is False:
                    rand = randint(1, 3)
                    restart = True

                elif self.__exit.get_rect().collidepoint(mouse_pos) & on_click1 == 1:
                    return

                if rand == 1:
                    win = self.__font.render("You Win!", 1, BLUE)
                    self.__screen.blit(win, (cup_one.centerx, cup_one.centery - 300, 50, 50))
                elif rand is not None:
                    lose = self.__font.render("You Lose :(", 1, BLUE)
                    self.__screen.blit(lose, (cup_one.centerx, cup_one.centery - 300, 50, 50))

            # Updates the screen
            pygame.display.flip()
