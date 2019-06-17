import random

from main.civilization.entities.base import BaseEntity
from main.map import utils


class Wisp(BaseEntity):
    def __init__(self, team, current_spot, destination_spot=None):
        super().__init__(team=team, current_spot=current_spot)

        self.destination_spot = destination_spot

    def set_destination(self, spot):
        self.destination_spot = spot

    def move(self, map_):
        # Move towards destination
        if self.destination_spot:
            new_coordinates = None

        # No destination - move randomly
        else:
            while True:
                new_coordinates = utils.add_coordinates(
                    self.get_current_position(),
                    random.choice(list(utils.DIRECTIONS.values()))
                )

                if map_.has_coordinates(new_coordinates) and map_.is_walkable(new_coordinates):
                    break

        new_spot = map_.get_spot(new_coordinates)

        # Delete from previous spot
        self.current_spot.remove_presence(self)

        self.current_spot = new_spot

        # Add to new spot
        self.current_spot.add_presence(self)
