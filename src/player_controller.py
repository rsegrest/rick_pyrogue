from src.input_model import InputModel
from events import Events
from src.view.level_view import LevelView
class PlayerController:

    def __init__(self, modelRef, viewRef):
        self.modelRef = modelRef
        self.viewRef = viewRef
        self.events = Events()
        self.events.on_change += LevelView.key_event

    def something_changed(self):
        print('Player Controller: something changed')
    
    # def 

    def move(self, direction):
        newPos = self.modelRef.getPosition()
        if (direction&InputModel.WEST) == InputModel.WEST:
            newPos[1] -= 1
        if (direction&InputModel.EAST) == InputModel.EAST:
            newPos[1] += 1
        if (direction&InputModel.SOUTH) == InputModel.SOUTH:
            newPos[0] += 1
        if (direction&InputModel.NORTH) == InputModel.NORTH:
            newPos[0] -= 1
        self.modelRef.setPosition(newPos)

    
    # def setPosition(self, newPos):
    #     self.position = newPos
    
    # @staticmethod
    # def getBitvalue():
    #     return self.modelRef.BITVALUE