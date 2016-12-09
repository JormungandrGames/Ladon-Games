import pygame

GAME_BAR_H_PERCENT = 0.03
SOUND_ICON_SIZE_PERCENT = 0.80
SCREEN_X = 0
FONT_MODIFIER = 30
# Volume is incremented or decremented by 10%
VOLUME_CHANGE = 0.1
FONT_H_ADJ = 4
GAME_BAR_COLOR = (70, 70, 70)
GAME_BAR_FONT_COLOR = (0, 0, 0)
START_X = 0
START_Y = 0
CLICKED = 1
# Volume gets set to 0 if muted
MUTE = 0.0
# Conversion of milliseconds to seconds
MS_TO_S = 0.001
ANTI_ALIASING = 1
SOUND_ICON_BUFFER = 5


class Game_Bar():
    def __init__(self, screen, game_title, game_score):
        # The height of the game bar
        # is a percentage of the game's screen
        self.__screen \
            = screen
        self.__game_bar_height \
            = GAME_BAR_H_PERCENT * screen.get_rect().height
        self.__game_bar_width \
            = screen.get_rect().width
        self.__game_bar_y_center = self.__game_bar_height / 2

        # Create the dimensions of the game bar
        self.__game_bar_size \
            = (START_X, START_Y, self.__game_bar_width, self.__game_bar_height)

        # Create the dimensions of the sound icons
        # image dimensions only accept ints
        # the dimensions must be converted
        self.__sound_icon_dim \
            = int(self.__game_bar_height)

        # Create the sound image icon
        self.__sound_icon \
            = pygame.image.load('game_skeleton/resources/images/volume_icon.png').convert_alpha()
        self.__sound_icon_size \
            = (self.__sound_icon_dim, self.__sound_icon_dim)
        self.__sound_icon \
            = pygame.transform.scale(self.__sound_icon, self.__sound_icon_size)
        self.__sound_icon_pos \
            = self.__sound_icon.get_rect()

        # Create the minus image icon
        self.__sound_minus_icon \
            = pygame.image.load('game_skeleton/resources/images/minus_icon.png').convert_alpha()
        self.__sound_minus_icon \
            = pygame.transform.scale(self.__sound_minus_icon, self.__sound_icon_size)
        self.__sound_minus_icon_pos \
            = self.__sound_minus_icon.get_rect()

        # Create the plus image icon's size
        self.__sound_plus_icon \
            = pygame.image.load('game_skeleton/resources/images/plus_icon.png').convert_alpha()
        self.__sound_plus_icon \
            = pygame.transform.scale(self.__sound_plus_icon, self.__sound_icon_size)
        self.__sound_plus_icon_pos \
            = self.__sound_plus_icon.get_rect()

        # Font for the game bar
        self.__f_game_bar_font \
            = pygame.font.SysFont('notosans',
                                  int(self.__game_bar_height - FONT_H_ADJ))

        # The game title and score
        self.__game_title \
            = game_title
        self.__game_score \
            = game_score
        self.__game_heading \
            = self.__game_title+": Score - "+str(self.__game_score)
        self.__f_game_heading \
            = self.__f_game_bar_font.render(self.__game_heading, ANTI_ALIASING,
                                            GAME_BAR_FONT_COLOR)
        self.__f_game_heading_pos \
            = self.__f_game_heading.get_rect()

        # Keep track of the game being muted or not.
        self.__muted = False

        # Keep track of the sounds playing
        self.__game_music_running = pygame.mixer.music.get_busy()
        self.__game_sound_running = pygame.mixer.get_busy()

        # Initialize the volumes
        self.__sound_effect_volume = 0
        self.__music_volume = 0

        # Get the game's FPS
        self.__clock = pygame.time.Clock()
        self.__fps\
            = str(self.__clock.get_fps())

        # Create the printing for "FPS"
        self.__f_fps\
            = self.__f_game_bar_font.render("FPS: ", ANTI_ALIASING, GAME_BAR_FONT_COLOR)
        self.__f_fps_pos \
            = self.__f_fps.get_rect()
        # Create the printing for the actual FPS integer
        self.__f_fps_num \
            = self.__f_game_bar_font.render(self.__fps, ANTI_ALIASING, GAME_BAR_FONT_COLOR)
        self.__f_fps_num_pos \
            = self.__f_fps_num.get_rect()

        # Constructor call
        self.__constructor()

    def __constructor(self):
        # Position the sound icon
        self.__sound_icon_pos.centery \
            = self.__game_bar_y_center
        self.__sound_icon_pos.centerx \
            = (self.__sound_icon_pos.width / 2) \
              + SOUND_ICON_BUFFER

        # Position the minus icon
        self.__sound_minus_icon_pos.centery \
            = self.__game_bar_y_center
        self.__sound_minus_icon_pos.centerx \
            = self.__sound_icon_pos.width \
              + (self.__sound_minus_icon_pos.width / 2) \
              + SOUND_ICON_BUFFER

        # Position the plus icon
        self.__sound_plus_icon_pos.centery \
            = self.__game_bar_y_center
        self.__sound_plus_icon_pos.centerx \
            = self.__sound_icon_pos.width \
              + self.__sound_minus_icon_pos.width \
              + (self.__sound_plus_icon_pos.width / 2) \
              + SOUND_ICON_BUFFER

        # Position the string of title and score
        self.__f_game_heading_pos.centery \
            = self.__game_bar_y_center
        self.__f_game_heading_pos.centerx \
            = self.__game_bar_width / 2

        # Position the string "FPS: "
        self.__f_fps_pos.centery \
            = self.__game_bar_y_center
        self.__f_fps_pos.centerx \
            = self.__game_bar_width \
              - self.__f_fps_pos.width \
              - self.__f_fps_num_pos.width

        # Position the FPS number
        self.__f_fps_num_pos.centery \
            = self.__game_bar_y_center
        self.__f_fps_num_pos.centerx \
            = self.__game_bar_width - self.__f_fps_num_pos.width

    def get_game_bar_height(self):
        return self.__game_bar_height

    def blit_game_bar(self, game_title, game_score='N/A'):
        fps = 60
        # Retrieve the game score each blit
        self.__game_score = game_score
        # Blit the game_bar
        pygame.draw.rect(self.__screen, GAME_BAR_COLOR, self.__game_bar_size)
        # Blit sound icons
        self.__screen.blit(self.__sound_icon, self.__sound_icon_pos)
        self.__screen.blit(self.__sound_plus_icon, self.__sound_plus_icon_pos)
        self.__screen.blit(self.__sound_minus_icon, self.__sound_minus_icon_pos)
        # Blit game title and score
        self.__game_title \
            = game_title
        self.__game_score \
            = game_score
        self.__game_heading = self.__game_title + ": Score - " + str(self.__game_score)
        self.__f_game_heading \
            = self.__f_game_bar_font.render(self.__game_heading, ANTI_ALIASING,
                                            GAME_BAR_FONT_COLOR)
        self.__screen.blit(self.__f_game_heading, self.__f_game_heading_pos)
        # Blit fps
        self.__fps \
            = str(self.__clock.get_fps())
        self.__f_fps_num \
            = self.__f_game_bar_font.render(self.__fps, ANTI_ALIASING, GAME_BAR_FONT_COLOR)
        self.__screen.blit(self.__f_fps, self.__f_fps_pos)
        self.__screen.blit(self.__f_fps_num, self.__f_fps_num_pos)
        self.__clock.tick(fps)

    def events(self, event):
        # Check for mouse click events
        mouse_pos = pygame.mouse.get_pos()

        # Captures the volume levels if the game is not currently muted
        if not self.__muted:
            if self.__game_sound_running:
                self.__sound_effect_volume \
                    = pygame.mixer.Sound.get_volume()
            if self.__game_music_running:
                self.__music_volume \
                    = pygame.mixer.music.get_volume()

        # Check for sound icon click for mute and un-mute
        if self.__sound_icon_pos.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONUP:
            # Game is not muted
            # then mute
            if not self.__muted:
                if self.__game_sound_running:
                    pygame.mixer.Sound.set_volume(MUTE)
                if self.__game_music_running:
                    pygame.mixer.music.set_volume(MUTE)
                self.__muted = True
            # Game is muted
            # then un-mute
            elif self.__muted:
                if self.__game_sound_running:
                    pygame.mixer.Sound.set_volume(self.__sound_effect_volume)
                if self.__game_music_running:
                    pygame.mixer.music.set_volume(self.__music_volume)
                self.__muted = False

        # Check for sound click for volume down
        if self.__sound_minus_icon_pos.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONUP:
            if self.__game_sound_running:
                pygame.mixer.Sound.set_volume(self.__sound_effect_volume - VOLUME_CHANGE)
            if self.__game_music_running:
                pygame.mixer.music.set_volume(self.__music_volume - VOLUME_CHANGE)

        # Check for sound click for volume up
        if self.__sound_plus_icon_pos.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONUP:
            if self.__game_sound_running:
                pygame.mixer.Sound.set_volume(self.__sound_effect_volume + VOLUME_CHANGE)
            if self.__game_music_running:
                pygame.mixer.music.set_volume(self.__music_volume + VOLUME_CHANGE)
