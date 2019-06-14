import pygame.sprite


class SpriteManager:
    def __init__(self):
        self.all_sprites = pygame.sprite.Group()

    def add_sprite(self, sprite):
        self.all_sprites.add(sprite)

    @staticmethod
    def kill_sprite(sprite):
        sprite.kill()

    def display_sprites(self, screen_surface, screen_surface_background):
        # Clear sprites on previous frame
        self.all_sprites.clear(screen_surface, screen_surface_background)

        # Update rectangles
        self.all_sprites.update()

        # Draw sprites
        self.all_sprites.draw(screen_surface)
