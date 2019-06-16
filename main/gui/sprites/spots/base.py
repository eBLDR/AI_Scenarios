import os

import pygame

from main import constants
from main.gui import utils


class BaseSpotSprite(pygame.sprite.Sprite):
    def __init__(self, spot, filename):
        super().__init__()

        self.spot = spot

        self.image_path = os.path.join(
            constants.IMG_SOURCE_PATH,
            '{filename}{size}x{size}.png'.format(
                filename=filename,
                size=constants.PIXELS_PER_BOX
            )
        )

        self.image = pygame.image.load(self.image_path).convert_alpha()

        self.rect = self.get_rect()

    def get_rect(self):
        return self.image.get_rect(
            center=utils.get_pixel_coordinates_from_map_coordinates(
                self.spot.coordinates, center=True)
        )

    def update(self):
        self.rect = self.get_rect()
