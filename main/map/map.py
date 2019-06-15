from main.map.spot import Spot


class Map:
    def __init__(self, width=None, height=None):
        self.dimensions = (width, height)

        self.coordinates_range = {
            'x': range(1, width + 1),
            'y': range(1, height + 1),
        }

        self.spots = [
            [Spot((y, x)) for y in self.coordinates_range['y']]
            for x in self.coordinates_range['x']
        ]

    def has_coordinates(self, coordinates):
        x, y = coordinates
        return (x in self.coordinates_range['x'] and
                y in self.coordinates_range['y'])

    def get_spot(self, coordinates):
        x, y = coordinates
        return self.spots[y - 1][x - 1]  # Map coordinates start at 1

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
