from gui.gui import GUI
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
            Civilization(self.map, team=1, gui=gui),
            Civilization(self.map, team=2, gui=gui),
            Civilization(self.map, team=3, gui=gui)
        ]

        # Link sprite group references
        if gui:
            self.gui.set_sprite_group_references(self.civilizations)

    def run(self):
        for i in range(self.generations):
            self.update_civilizations()

            if self.gui:
                self.update_gui()

    def update_civilizations(self):
        for civilization in self.civilizations:
            civilization.update_civilization()

    def update_gui(self):
        self.gui.update_frame()
