from gui.sprites.base import BaseSprite


class WispSprite(BaseSprite):
    def __init__(self, wisp_object):
        super().__init__(wisp_object, filename='wisp')
