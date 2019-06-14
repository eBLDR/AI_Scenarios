import pygame

from gui import constants, utils


class Screen:
    def __init__(self, scenario_map, background_color):
        self.scenario_map = scenario_map

        self.screen_size = utils.get_pixel_coordinates_from_map_coordinates(
            self.scenario_map.dimensions
        )

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
        self.draw_grid()

        # Set screen background
        self.screen_surface_background = self.screen_surface.copy()

    def draw_grid(self):
        # Vertical lines
        for x in range(self.scenario_map.dimensions[0]):
            pygame.draw.line(
                self.screen_surface,
                constants.COLORS['BLACK'],
                utils.get_pixel_coordinates_from_map_coordinates((x, 0)),
                utils.get_pixel_coordinates_from_map_coordinates(
                    (x, self.screen_size[1])
                ),
                1
            )

        # Horizontal lines
        for y in range(self.scenario_map.dimensions[1]):
            pygame.draw.line(
                self.screen_surface,
                constants.COLORS['BLACK'],
                utils.get_pixel_coordinates_from_map_coordinates((0, y)),
                utils.get_pixel_coordinates_from_map_coordinates(
                    (self.screen_size[0], y)
                ),
                1
            )
