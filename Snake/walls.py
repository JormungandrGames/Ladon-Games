import pygame

# Wall Variables
WALL_COLOR = (255, 0, 0)
WALL_HEIGHT = 10


class BuildWalls:
    def __init__(self, screen):
        self.__screen = screen
        self.__wall_size = int(screen.get_rect().height / 1.5)
        self.__north_wall_x = screen.get_rect().centerx - (self.__wall_size / 2)
        self.__north_wall_y = screen.get_rect().centery - (self.__wall_size / 2)
        self.__east_wall_x = screen.get_rect().centerx + (self.__wall_size / 2)
        self.__east_wall_y = screen.get_rect().centery - (self.__wall_size / 2)
        self.__south_wall_x = screen.get_rect().centerx - (self.__wall_size / 2)
        self.__south_wall_y = screen.get_rect().centery + (self.__wall_size / 2)
        self.__west_wall_x = screen.get_rect().centerx - (self.__wall_size / 2)
        self.__west_wall_y = screen.get_rect().centery - (self.__wall_size / 2)
        self.__walls = []

    def blit(self):
        north_rect = pygame.Rect(self.__north_wall_x, self.__north_wall_y, self.__wall_size + 10, WALL_HEIGHT)
        pygame.draw.rect(self.__screen, WALL_COLOR, north_rect)
        self.__walls.append(north_rect)
        east_rect = pygame.Rect(self.__east_wall_x, self.__east_wall_y, WALL_HEIGHT, self.__wall_size + 10)
        pygame.draw.rect(self.__screen, WALL_COLOR, east_rect)
        self.__walls.append(east_rect)
        south_rect = pygame.Rect(self.__south_wall_x, self.__south_wall_y, self.__wall_size + 10, WALL_HEIGHT)
        pygame.draw.rect(self.__screen, WALL_COLOR, south_rect)
        self.__walls.append(south_rect)
        west_rect = pygame.Rect(self.__west_wall_x, self.__west_wall_y, WALL_HEIGHT, self.__wall_size + 10)
        pygame.draw.rect(self.__screen, WALL_COLOR, west_rect)
        self.__walls.append(west_rect)

        return self.__walls

