from main.map.spots.base import Base


class Obstacle(Base):
    def __init__(self, coordinates):
        super().__init__(coordinates, walkable=False)
