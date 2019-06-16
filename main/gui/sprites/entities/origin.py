from main.gui.sprites.entities.base import BaseEntitySprite


class OriginSprite(BaseEntitySprite):
    def __init__(self, origin_object):
        super().__init__(origin_object, filename='origin')
