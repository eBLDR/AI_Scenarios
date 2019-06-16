class BaseEntity:
    def __init__(self, team, current_spot):
        self.team = team
        self.current_spot = None

        self.spawn(current_spot)

    def get_current_position(self):
        return self.current_spot.coordinates

    def spawn(self, spot):
        self.current_spot = spot
        self.current_spot.add_presence(self)
