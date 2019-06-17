import pygame

from main import constants
from main.gui.screen.screen import Screen
from main.gui.sprites.manager import SpriteManager


class GUI:
    def __init__(
            self,
            map_,
            scenario_name,
            background_color=constants.COLORS['WHITE']
    ):
        self.scenario_name = scenario_name

        self.source_path = constants.IMG_SOURCE_PATH

        self.screen = Screen(map_, background_color=background_color)

        self.sprite_manager = SpriteManager()

        self.font_size = 24
        self.font = pygame.font.SysFont('Roboto Mono', self.font_size)

        self.fps = constants.FPS
        self.clock = pygame.time.Clock()

    def set_sprite_group_references(self, map_sprites, civilizations):
        # Civilization sprites
        self.sprite_manager.entity_groups = [
            civilization.sprites for civilization in civilizations
        ]

        # Map sprites
        self.sprite_manager.map_groups.append(map_sprites)

    def update_frame(self, civilizations, generation):
        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

        # Display sprites
        self.sprite_manager.display_sprites(
            self.screen.screen_surface, self.screen.screen_surface_background
        )

        # Render text
        self.render_text(civilizations)

        pygame.display.set_caption(
            'Scenario: {} | Generation: {}'.format(
                self.scenario_name,
                generation)
        )

        pygame.display.update()

        # FPS timer
        self.clock.tick(self.fps)

    def render_text(self, civilizations):
        stats_width = constants.SCREEN_SIZE[0] // len(civilizations)
        for count_civ, civilization in enumerate(civilizations):
            for count_line, line in enumerate(str(civilization).split('\n')):
                text = self.font.render(
                    line,
                    False,
                    constants.COLORS['BLACK']
                )
                self.screen.render_text(
                    text,
                    (count_civ * stats_width, count_line * self.font_size)
                )
