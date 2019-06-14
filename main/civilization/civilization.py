from main.civilization.entity import Entity


class Civilization:
    def __init__(self, map_, team=1):
        self.map = map_
        self.team = team
        self.entities = []

    def get_entities(self):
        return self.entities

    def create_entity(self, coordinates):
        new_entity = Entity(
            self.team,
            self.map.get_spot(coordinates)
        )
        self.entities.append(new_entity)
        return new_entity

    def remove_entity(self, entity):
        self.entities.remove(entity)

    def update_civilization(self):
        # Move entities
        for entity in self.entities:
            entity.move(self.map)

    def broadcast_order(self):
        # set heading to all
        pass