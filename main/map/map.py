from main.map.spots.spot import Spot
from main.map.spots.sources.energy import EnergySource
from main.map.spots.obstacle import Obstacle


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
        for source_config in self.config['sources']:
            source = None
            source_sprite = None

            if source_config['type'] == 'energy':
                source = EnergySource(
                    (source_config['x'], source_config['y']),
                )

                if self.sprites is not None:
                    from main.gui.sprites.spots.source import EnergySourceSprite
                    source_sprite = EnergySourceSprite(source)

            if source:
                self.add_special_spot(
                    source,
                    spot_sprite=source_sprite
                )

        # Obstacles
        for obstacle_config in self.config['obstacles']:
            obstacle = Obstacle(
                (obstacle_config['x'], obstacle_config['y'])
            )
            obstacle_sprite = None

            if self.sprites is not None:
                from main.gui.sprites.spots.obstacle import ObstacleSprite
                obstacle_sprite = ObstacleSprite(obstacle)

            self.add_special_spot(
                obstacle,
                spot_sprite=obstacle_sprite
            )

    def get_width(self):
        return self.dimensions['width']

    def get_height(self):
        return self.dimensions['height']

    def add_special_spot(self, spot, spot_sprite=None):
        self.spots[spot.coordinates[1] - 1][spot.coordinates[0] - 1] = spot

        if self.sprites is not None:
            self.sprites.add(spot_sprite)

    # Map interaction
    def has_coordinates(self, coordinates):
        x, y = coordinates
        return (x in self.coordinates_range['x'] and
                y in self.coordinates_range['y'])

    def get_spot(self, coordinates):
        x, y = coordinates
        return self.spots[y - 1][x - 1]  # Map coordinates start at 1

    def is_walkable(self, coordinates):
        return self.get_spot(coordinates).is_walkable()

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
