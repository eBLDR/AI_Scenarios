import pygame

from gui import constants
from gui.screen.screen import Screen
from gui.sprites.spritemanager import SpriteManager


class GUI:
    def __init__(self, scenario_map, fps=1, background_color=constants.COLORS['WHITE']):
        pygame.init()

        self.source_path = constants.SOURCE_PATH

        self.screen = Screen(scenario_map, background_color=background_color)

        self.sprite_manager = SpriteManager()

        self.fps = fps
        self.clock = pygame.time.Clock()

    def update_frame(self):
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

        pygame.display.update()

        # FPS timer
        self.clock.tick(self.fps)