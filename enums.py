from enum import Enum


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
GREEN_LIGHT = (128, 255, 0)
GREEN_DARK = (0, 153, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW_LIGHT = (255, 255, 102)
YELLOW = (255, 255, 0)
GREY = (211, 211, 211)
ORANGE = (255, 69, 0)
PINK = (255, 105, 180)
BROWN = (153, 76, 0)
BROWN_LIGHT = (204, 102, 0)

class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

