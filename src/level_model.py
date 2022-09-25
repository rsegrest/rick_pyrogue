from src.player_model import PlayerModel

class LevelModel:
    def __init__(self):
        self.level = 1
        self.playerModel = PlayerModel()
        self.layout = self.generateTestLayout()
        self.placePlayer([2,2])

    def generateTestLayout(self):
        layout = self.generateTestRoom()
        # playerPos = self.playerModel.getPosition()
        return layout

    def generateTestRoom(self):
        room = [
            [1,1,1,1,1],
            [1,0,0,0,1],
            [1,0,0,0,1],
            [1,0,0,0,1],
            [1,1,1,1,1],
        ]
        return room
    
    def placePlayer(self, pos):
        print('placing player at: ', pos)
        self.layout[pos[0]][pos[1]] = '☻'
        print(self.layout)

    def update(self):
        self.layout = self.generateTestLayout()
        latestPlayerPos = self.playerModel.getPosition()
        print('latestPlayerPos: ', latestPlayerPos)
        self.placePlayer(latestPlayerPos)