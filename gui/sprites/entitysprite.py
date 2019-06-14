import os

import pygame

from gui import constants, utils


class EntitySprite(pygame.sprite.Sprite):
    def __init__(self, entity):
        super().__init__()

        self.entity = entity

        self.image_path = os.path.join(
            constants.SOURCE_PATH,
            'wisp20x20{color}.png'.format(
                color=constants.TEAM_COLOR[self.entity.team]
            )
        )

        self.image = pygame.image.load(self.image_path).convert_alpha()

        self.rect = self.get_rect()

        # If mask collision is intended
        self.mask = pygame.mask.from_surface(self.image)

    def get_rect(self):
        return self.image.get_rect(
            center=utils.get_pixel_coordinates_from_map_coordinates(
                self.entity.get_current_position(), center=True)
        )

    def update(self):
        self.rect = self.get_rect()
