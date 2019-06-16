class Resources:
    types = [
        'energy'
    ]

    def __init__(self):
        self._energy = 0

    def has_resources(self):
        for resource in self.types:
            if getattr(self, '{}'.format(resource)) > 0:
                return True

        return False

    # Getters and setters
    @property
    def energy(self):
        return self._energy

    @energy.setter
    def energy(self, energy):
        self._energy = energy

    def has_enough_resources(self, energy=None):
        if self.energy < energy:
            return False

        return True
