from main.map.spots.base import Base


class Spot(Base):
    def __init__(self, coordinates):
        super().__init__(coordinates, walkable=True)
        self.presences = []

    def add_presence(self, entity):
        self.presences.append(entity)

    def has_presences(self):
        return bool(self.presences)

    def get_presences(self):
        return self.presences

    def remove_presence(self, entity):
        self.presences.remove(entity)

    def remove_all_presences(self):
        self.presences = []
