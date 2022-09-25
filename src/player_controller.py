
class PlayerController:

    WEST = 0x01
    EAST = 0x02
    NORTH = 0x04
    SOUTH = 0x08
    NW = NORTH|WEST
    NE = NORTH|EAST
    SW = SOUTH|WEST
    SE = SOUTH|EAST




    def __init__(self, modelRef):
        self.modelRef = modelRef

    def move(self, direction):
        newPos = self.modelRef.getPosition()
        if (direction&PlayerController.WEST) == PlayerController.WEST:
            newPos[1] -= 1
        if (direction&PlayerController.EAST) == PlayerController.EAST:
            newPos[1] += 1
        if (direction&PlayerController.SOUTH) == PlayerController.SOUTH:
            newPos[0] += 1
        if (direction&PlayerController.NORTH) == PlayerController.NORTH:
            newPos[0] -= 1
        self.modelRef.setPosition(newPos)

    
    # def setPosition(self, newPos):
    #     self.position = newPos
    
    # @staticmethod
    # def getBitvalue():
    #     return self.modelRef.BITVALUE