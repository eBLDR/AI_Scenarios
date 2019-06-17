class SpriteManager:
    def __init__(self,):
        self.map_groups = []
        self.entity_groups = []

    @staticmethod
    def kill_sprite(sprite):
        sprite.kill()

    def display_sprites(self, screen_surface, screen_surface_background):
        # Display map first
        for sprite_group in self.map_groups:
            self.display_group(
                sprite_group, screen_surface, screen_surface_background
            )

        # Then entities
        for sprite_group in self.entity_groups:
            self.display_group(
                sprite_group, screen_surface, screen_surface_background
            )

    @staticmethod
    def display_group(sprite_group, screen_surface, screen_surface_background):
        # Clear sprites on previous frame
        sprite_group.clear(screen_surface, screen_surface_background)

        # Update rectangles
        sprite_group.update()

        # Draw sprites
        sprite_group.draw(screen_surface)