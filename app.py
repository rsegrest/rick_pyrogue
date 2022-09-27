import curses
from src.level_model import LevelModel
from src.player_model import PlayerModel
from src.player_controller import PlayerController
from src.view.level_view import LevelView
from events import Events

if __name__=='__main__':
    levelModel = LevelModel()
    playerController = PlayerController(levelModel.playerModel)
    levelView = LevelView(levelModel.layout, playerController, levelModel)
    # playerController.move(PlayerController.WEST)
    print(levelModel.playerModel.getPosition())
    levelModel.update() # move this to the controller
    # print(levelModel.layout)
    while(True):
        
        curses.wrapper(levelView.draw_stuff)
        

        # # Loop where k is the last character pressed
        # while (k != ord('q')):

        #     # Initialization
        #     stdscr.clear()
        #     height, width = stdscr.getmaxyx()

        #     if k == curses.KEY_DOWN:
        #         cursor_y = cursor_y + 1
        #     elif k == curses.KEY_UP:
        #         cursor_y = cursor_y - 1
        #     elif k == curses.KEY_RIGHT:
        #         cursor_x = cursor_x + 1
        #     elif k == curses.KEY_LEFT:
        #         cursor_x = cursor_x - 1
