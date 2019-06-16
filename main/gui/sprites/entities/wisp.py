from main.gui.sprites.entities.base import BaseEntitySprite


class WispSprite(BaseEntitySprite):
    def __init__(self, wisp_object):
        super().__init__(wisp_object, filename='wisp')
