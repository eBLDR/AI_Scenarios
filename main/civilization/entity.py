import random

from main.map import utils


class Entity:
    def __init__(self, team, current_spot, destination_spot=None):
        self.team = team
        self.current_spot = None

        self.destination_spot = destination_spot

        self.spawn(current_spot)

    def get_current_position(self):
        return self.current_spot.coordinates

    def set_destination(self, spot):
        self.destination_spot = spot

    def spawn(self, spot):
        self.current_spot = spot
        self.current_spot.add_presence(self)

    def move(self, map_):
        current_coordinates = self.get_current_position()

        # Move towards destination
        if self.destination_spot:
            new_spot = None

        # No destination - move randomly
        else:
            new_coordinates = utils.add_coordinates(
                current_coordinates,
                random.choice(list(utils.DIRECTIONS.values()))
                # max_=map_.dimensions
            )
            new_spot = map_.get_spot(new_coordinates)

        # Delete from previous spot
        self.current_spot.remove_presence(self)

        self.current_spot = new_spot

        # Add to new spot
        self.current_spot.add_presence(self)
