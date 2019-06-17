class Base:
    def __init__(self, coordinates, walkable):
        self.coordinates = coordinates
        self.walkable = walkable

    def is_walkable(self):
        return self.walkable
