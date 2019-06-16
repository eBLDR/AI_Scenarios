import random

from main.civilization.entities.wisp import Wisp
from main.civilization.entities.origin import Origin
from main.resources.resources import Resources


class Civilization:
    def __init__(self, map_, config, gui=True):
        # Attributes
        self.map = map_
        self.team = None
        self.origin = None
        self.resources = Resources()
        self.wisps = []

        # GUI
        if gui:
            from pygame.sprite import Group
            self.sprites = Group()
        else:
            self.sprites = None

        # Load from config
        self.load_civilization(config)

    def load_civilization(self, config):
        # Team
        self.team = config['team']

        # Origin
        for origin in config['origin']:
            self.create_origin(
                self.map.get_spot(
                    (origin['x'],
                     origin['y'])
                )
            )

        # Resources
        self.resources.energy = config['resources'].get('energy', 0)

    def create_origin(self, spot):
        origin = Origin(self.team, spot)

        if self.sprites is not None:
            from main.gui.sprites.entities.origin import OriginSprite
            self.sprites.add(
                OriginSprite(origin)
            )

        self.origin = origin

    def create_wisp(self):
        wisp = Wisp(
            self.team,
            self.origin.current_spot
        )

        if self.sprites is not None:
            from main.gui.sprites.entities.wisp import WispSprite
            self.sprites.add(
                WispSprite(wisp)
            )

        self.wisps.append(wisp)

    def get_wisps(self):
        return self.wisps

    def remove_wisp(self, wisp):
        self.wisps.remove(wisp)

    def update_civilization(self):
        # Generate wisp
        if random.random() > 0.2:
            self.create_wisp()

        # Move wisps
        for wisp in self.wisps:
            wisp.move(self.map)

    def broadcast_order(self):
        # set heading to all
        pass
