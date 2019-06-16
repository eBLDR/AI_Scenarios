import pygame

from main import constants
from main.gui import utils


class Screen:
    def __init__(self, scenario_map, background_color):
        self.map = scenario_map

        self.screen_size = constants.SCREEN_SIZE

        self.screen_surface = pygame.display.set_mode(self.screen_size, 0, 32)

        pygame.display.set_caption('AI Scenarios')

        # icon = pygame.image.load(os.path.join(
        #     constants.SOURCE_PATH,
        #     'wisp20x20red.png')
        # )

        # pygame.display.set_icon(icon)

        self.screen_surface_background = None

        self.init_screen(background_color)

    def init_screen(self, background_color):
        self.screen_surface.fill(background_color)
        self.draw_separation_bar()
        self.draw_map_grid()

        # Set screen background
        self.screen_surface_background = self.screen_surface.copy()

    def draw_separation_bar(self):
        separation_bar_width = 3
        pygame.draw.rect(
            self.screen_surface,
            constants.COLORS['BLACK'],
            (
                0,
                constants.MENU_HEIGHT - separation_bar_width,
                self.screen_size[0],
                separation_bar_width
            )
        )

    def draw_map_grid(self):
        # Vertical lines
        for x in self.map.coordinates_range['x']:
            pygame.draw.line(
                self.screen_surface,
                constants.COLORS['BLACK'],
                utils.get_pixel_coordinates_from_map_coordinates((x, 0)),
                utils.get_pixel_coordinates_from_map_coordinates(
                    (x, self.map.get_height())
                ),
                1
            )

        # Horizontal lines
        for y in self.map.coordinates_range['y']:
            pygame.draw.line(
                self.screen_surface,
                constants.COLORS['BLACK'],
                utils.get_pixel_coordinates_from_map_coordinates((0, y)),
                utils.get_pixel_coordinates_from_map_coordinates(
                    (self.map.get_width(), y)
                ),
                1
            )
