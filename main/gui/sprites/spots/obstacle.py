from main.gui.sprites.spots.base import BaseSpotSprite


class ObstacleSprite(BaseSpotSprite):
    def __init__(self, obstacle_object):
        super().__init__(obstacle_object, filename='obstacle')
