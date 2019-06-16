from main.civilization.civilization import Civilization
from main.gui.gui import GUI
from main.map.map import Map
from main.scenarios.manager import ScenarioManager


class Manager:
    def __init__(self, scenario_name, gui=True):
        self.generations = None
        self.map = None
        self.civilizations = []
        self.gui = None

        if gui:
            import pygame
            pygame.init()

        # Load scenario
        self.load_scenario(scenario_name, gui)

    def load_scenario(self, scenario_name, gui):
        scenario_manager = ScenarioManager(scenario_name)

        self.generations = scenario_manager.get_generations()

        # Map initialization
        self.map = Map(scenario_manager.get_map_config())

        # GUI initialization
        self.gui = GUI(self.map) if gui else None

        # Map construction
        self.map.build_map()

        # Civilization initialization
        for civilization_config in scenario_manager.get_civilizations_config():
            self.civilizations.append(
                Civilization(self.map, civilization_config, gui=gui)
            )

        # Link sprite group references
        if gui:
            self.gui.set_sprite_group_references(
                self.map.sprites, self.civilizations
            )

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
