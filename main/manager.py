from gui.gui import GUI
from gui.sprites.entitysprite import EntitySprite
from main.civilization.civilization import Civilization
from main.map.map import Map


class Manager:
    def __init__(self, map_size, generations, gui=True):
        self.generations = generations

        # Map management
        self.map = Map(map_size, map_size)

        # GUI management
        self.gui = GUI(self.map) if gui else None

        # Civilization management
        self.civilizations = [
            Civilization(self.map)
        ]

    def run(self):
        # TMP
        self.civilizations[0].create_entity((4, 4))

        wisp_sprite = EntitySprite(self.civilizations[0].entities[0])
        self.gui.sprite_manager.add_sprite(wisp_sprite)

        for i in range(self.generations):
            self.update_civilizations()

            if self.gui:
                self.update_gui()

    def update_civilizations(self):
        for civilization in self.civilizations:
            civilization.update_civilization()

    def update_gui(self):
        self.gui.update_frame()
