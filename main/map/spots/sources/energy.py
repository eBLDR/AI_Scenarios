from main.map.spots.sources.base import BaseSource


class EnergySource(BaseSource):
    def extract(self, amount):
        extracted = amount if amount >= self.resources.energy \
            else self.resources.energy
        self.resources.energy -= amount
        return extracted
