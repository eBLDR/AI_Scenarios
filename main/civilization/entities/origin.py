from main.civilization.entities.base import BaseEntity


class Origin(BaseEntity):
    def __init__(self, team, current_spot):
        super().__init__(team=team, current_spot=current_spot)
