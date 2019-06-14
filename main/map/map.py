from main.map.spot import Spot


class Map:
    def __init__(self, width=None, height=None):
        self.dimensions = (width, height)
        self.spots = [
            [Spot((y, x)) for y in range(1, self.dimensions[1] + 1)]
            for x in range(1, self.dimensions[0] + 1)
        ]

    def get_spot(self, coordinates):
        x, y = coordinates
        # Map coordinates start at 1
        return self.spots[y - 1][x - 1]

    def has_presences(self, coordinates):
        return self.get_spot(coordinates).has_presences()

    def get_presences(self, coordinates):
        return self.get_spot(coordinates).get_presences()

    def add_presence(self, coordinates, entity):
        self.get_spot(coordinates).add_presence(entity)

    def remove_presence(self, coordinates, entity):
        self.get_spot(coordinates).remove_presence(entity)

    def remove_all_presences(self, coordinates):
        self.get_spot(coordinates).remove_all_presences()
