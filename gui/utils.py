from gui import constants


def get_pixel_coordinates_from_map_coordinates(map_coordinates, center=False):
    return (
        map_coordinates[0] * constants.PIXELS_PER_BOX,
        map_coordinates[1] * constants.PIXELS_PER_BOX
    ) if not center else (
        map_coordinates[0] * constants.PIXELS_PER_BOX - constants.PIXELS_PER_BOX // 2,
        map_coordinates[1] * constants.PIXELS_PER_BOX - constants.PIXELS_PER_BOX // 2
    )
