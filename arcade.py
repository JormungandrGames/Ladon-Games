#!/usr/bin/python

import pygame

from resolution_settings import *


def main():
    resolution = SettingsMenu()
    resolution.load_menu_objects()


if __name__ == '__main__':
    main()
