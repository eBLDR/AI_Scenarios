from gui.sprites.base import BaseSprite


class OriginSprite(BaseSprite):
    def __init__(self, origin_object):
        super().__init__(origin_object, filename='origin')
