class Spot:
    def __init__(self, coordinates):
        self.coordinates = coordinates
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
