class InputModel:
    WEST = 0x01
    EAST = 0x02
    NORTH = 0x04
    SOUTH = 0x08
    NW = NORTH|WEST
    NE = NORTH|EAST
    SW = SOUTH|WEST
    SE = SOUTH|EAST