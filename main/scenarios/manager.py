import json
import os

from main import constants


class ScenarioManager:
    def __init__(self, scenario_name):
        self.file_path = None
        self.config = None

        self.set_filename(scenario_name)
        self.load_config()

    def set_filename(self, scenario_name):
        self.file_path = os.path.join(
            constants.SCENARIO_CONFIG_PATH,
            '{}.json'.format(scenario_name)
        )

    def load_config(self):
        with open(self.file_path, 'r') as file:
            self.config = json.load(file)

    def get_generations(self):
        return self.config['generations']

    def get_map_config(self):
        return self.config['map']

    def get_civilizations_config(self):
        return self.config['civilizations']
