import random

from main.civilization.wisp import Wisp
from main.civilization.origin import Origin


class Civilization:
    def __init__(self, map_, team, gui=True):
        self.map = map_
        self.team = team

        self.origin = None
        self.wisps = []

        # GUI
        if gui:
            from pygame.sprite import Group
            self.sprites = Group()
        else:
            self.sprites = None

        self.init_civilization()

    def init_civilization(self):
        origin_coordinates = (
            random.randint(1, self.map.dimensions[0]),
            random.randint(1, self.map.dimensions[1])
        )

        origin = Origin(
            self.team,
            self.map.get_spot(origin_coordinates)
        )

        if self.sprites is not None:
            from gui.sprites.origin import OriginSprite
            self.sprites.add(
                OriginSprite(origin)
            )

        self.origin = origin

    def get_wisps(self):
        return self.wisps

    def create_wisp(self):
        wisp = Wisp(
            self.team,
            self.origin.current_spot
        )

        if self.sprites is not None:
            from gui.sprites.wisp import WispSprite
            self.sprites.add(
                WispSprite(wisp)
            )

        self.wisps.append(wisp)

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
