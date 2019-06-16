import os

# ENVIRONMENT
BASE_DIR = os.path.join(os.getcwd(), 'main')
SCENARIO_CONFIG_PATH = os.path.join(BASE_DIR, 'scenarios', 'config')

# GUI
IMG_SOURCE_PATH = os.path.join(BASE_DIR, 'gui', 'src')
SCREEN_SIZE = (800, 800)
FPS = 3

MOUSE_LEFT = 1
MOUSE_RIGHT = 3

COLORS = {
    'BLACK': (0, 0, 0),
    'WHITE': (255, 255, 255),
    'GRAY': (128, 128, 128),
    'RED': (255, 0, 0),
    'GREEN': (0, 255, 0),
    'BLUE': (0, 0, 155),
    'YELLOW': (255, 255, 0)
}

TEAM_COLOR = {
    1: 'red',
    2: 'blue',
    3: 'green'
}

# Sprite images available: [10px, 20px]
PIXELS_PER_BOX = 20

MENU_HEIGHT = 100
