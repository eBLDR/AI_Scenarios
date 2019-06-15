class SpriteManager:
    def __init__(self,):
        self.all_groups = []

    @staticmethod
    def kill_sprite(sprite):
        sprite.kill()

    def display_sprites(self, screen_surface, screen_surface_background):
        for sprite_group in self.all_groups:
            # Clear sprites on previous frame
            sprite_group.clear(screen_surface, screen_surface_background)

            # Update rectangles
            sprite_group.update()

            # Draw sprites
            sprite_group.draw(screen_surface)
