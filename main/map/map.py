from main.map.spot import Spot
from main.map.sources.energy import EnergySource


class Map:
    def __init__(self, config, gui=True):
        self.config = config

        # Attributes
        self.dimensions = {
            'width': self.config['size']['width'],
            'height': self.config['size']['height']
        }

        self.coordinates_range = {
            'x': range(1, self.get_width() + 1),
            'y': range(1, self.get_height() + 1),
        }

        self.obstacles = []
        self.spots = []

        # GUI
        if gui:
            from pygame.sprite import Group
            self.sprites = Group()
        else:
            self.sprites = None

    def build_map(self):
        # Build main terrain
        self.spots = [
            [Spot((x, y)) for x in self.coordinates_range['x']]
            for y in self.coordinates_range['y']
        ]

        # Sources
        for source in self.config['sources']:
            source_ = None
            source_sprite = None

            if source['type'] == 'energy':
                source_ = EnergySource(
                    (source['x'], source['y']),
                )

                if self.sprites is not None:
                    from main.gui.sprites.spots.source import EnergySourceSprite
                    source_sprite = EnergySourceSprite(source_)

            if source_:
                self.add_source(
                    source_,
                    source_sprite=source_sprite
                )

        # Obstacles

    def get_width(self):
        return self.dimensions['width']

    def get_height(self):
        return self.dimensions['height']

    def add_source(self, source, source_sprite=None):
        self.spots[source.coordinates[1]][source.coordinates[0]] = source

        if self.sprites is not None:
            self.sprites.add(source_sprite)

    # Map interaction
    def has_coordinates(self, coordinates):
        x, y = coordinates
        return (x in self.coordinates_range['x'] and
                y in self.coordinates_range['y'])

    def get_spot(self, coordinates):
        x, y = coordinates
        return self.spots[y - 1][x - 1]  # Map coordinates start at 1

    def add_presence(self, coordinates, entity):
        self.get_spot(coordinates).add_presence(entity)

    def has_presences(self, coordinates):
        return self.get_spot(coordinates).has_presences()

    def get_presences(self, coordinates):
        return self.get_spot(coordinates).get_presences()

    def remove_presence(self, coordinates, entity):
        self.get_spot(coordinates).remove_presence(entity)

    def remove_all_presences(self, coordinates):
        self.get_spot(coordinates).remove_all_presences()
