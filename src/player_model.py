from src.attributes_model import Attributes 

class PlayerModel:

    BITVALUE = 0o02000

    def __init__(self):
        self.currentPosition = [2,2]
        self.name = 'Whistlebritches'
        self.attributes = Attributes()

    # CRUD operations in a model
    # "Read"
    def getPosition(self):
        return self.currentPosition

    # "Update"
    def setPosition(self, newPos):
        self.currentPosition = newPos
    
    @staticmethod
    def getBitvalue():
        return PlayerModel.BITVALUE