from main import constants


def get_pixel_coordinates_from_map_coordinates(map_coordinates, center=False):
    """
    If center is False, will return bottom right corner.
    :param map_coordinates:
    :param center:
    :return:
    """
    x_pixel = (map_coordinates[0] * constants.PIXELS_PER_BOX)
    y_pixel = (
            constants.MENU_HEIGHT
            + map_coordinates[1] * constants.PIXELS_PER_BOX
    )

    return (
        x_pixel,
        y_pixel
    ) if not center else (
        x_pixel - constants.PIXELS_PER_BOX // 2,
        y_pixel - constants.PIXELS_PER_BOX // 2
    )
