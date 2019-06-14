DIRECTIONS = {
    'NORTH': (0, -1),
    'SOUTH': (0, 1),
    'EAST': (1, 0),
    'WEST': (-1, 0)
}


def add_coordinates(coordinates_1, coordinates_2):
    return (
        coordinates_1[0] + coordinates_2[0],
        coordinates_1[1] + coordinates_2[1]
    )
