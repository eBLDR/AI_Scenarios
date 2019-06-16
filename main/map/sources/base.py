from main.map.spot import Spot
from main.resources.resources import Resources


class BaseSource(Spot):
    def __init__(self, coordinates):
        super().__init__(coordinates)
        self.resources = Resources()

    def extract(self, amount):
        raise NotImplementedError
