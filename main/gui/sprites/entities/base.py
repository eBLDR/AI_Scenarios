import os

import pygame

from main import constants
from main.gui import utils


class BaseEntitySprite(pygame.sprite.Sprite):
    def __init__(self, entity, filename):
        super().__init__()

        self.entity = entity

        self.image_path = os.path.join(
            constants.IMG_SOURCE_PATH,
            '{filename}{size}x{size}{color}.png'.format(
                filename=filename,
                size=constants.PIXELS_PER_BOX,
                color=constants.TEAM_COLOR[self.entity.team]
            )
        )

        self.image = pygame.image.load(self.image_path).convert_alpha()

        self.rect = self.get_rect()

    def get_rect(self):
        return self.image.get_rect(
            center=utils.get_pixel_coordinates_from_map_coordinates(
                self.entity.get_current_position(), center=True)
        )

    def update(self):
        self.rect = self.get_rect()
