from src.level_model import LevelModel
from src.player_model import PlayerModel
from src.player_controller import PlayerController
from src.view.level_view import LevelView

if __name__=='__main__':
    levelModel = LevelModel()
    playerController = PlayerController(levelModel.playerModel)
    levelView = LevelView()
    playerController.move(PlayerController.WEST)
    print(levelModel.playerModel.getPosition())
    levelModel.update() # move this to the controller
    # print(levelModel.layout)
    levelView.draw_stuff(levelModel.layout)
