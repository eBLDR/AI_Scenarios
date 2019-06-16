from main.gui.sprites.spots.base import BaseSpotSprite


class EnergySourceSprite(BaseSpotSprite):
    def __init__(self, source_object):
        super().__init__(source_object, filename='energy_source')
