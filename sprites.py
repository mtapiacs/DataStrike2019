"""
This module is used to pull individual sprites from sprite sheets.
http://programarcadegames.com/python_examples/en/sprite_sheets/
"""
import pygame


class SpriteSheet(object):
    """ Class used to grab images out of a sprite sheet. """

    def __init__(self, file_name):
        """ Constructor. Pass in the file name of the sprite sheet. """

        # Load the sprite sheet.
        self.sprite_sheet = pygame.image.load(file_name).convert()

    def get_image(self, x, y, width, height, color):
        """ Grab a single image out of a larger spritesheet
            Pass in the x, y location of the sprite
            and the width and height of the sprite. """

        # Create a new blank image
        image = pygame.Surface([40, 40], pygame.SRCALPHA).convert()
        image.fill(color)
        # Copy the sprite from the large sheet onto the smaller image
        image.blit(self.sprite_sheet, (7, 7), (x, y, width, height))

        # Assuming black works as the transparent color
        # image.set_colorkey((255,255,255))

        # Return the image
        return image
