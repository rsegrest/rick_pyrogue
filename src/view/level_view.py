import curses
from src.ascii_helper import ASCII_Helper as ascii
from src.player_controller import PlayerController
# wrapper

class LevelView:
    def __init__(self, initial_layout, playerController, levelModel):
        self.layout = initial_layout
        self.playerController = playerController
        self.levelModel = levelModel

    def set_player_pos(self, pos):
        self.playerPos = pos

    def render_field(self, stdscr):
        stdscr.clear()
        curses.curs_set(0)
        counter = 0
        index = 0
        row = 0
        col = 0
        for r in self.layout:
            for c in r:
                counter += 1
                # if row == self.playerPos[0] and col == self.playerPos[1]:
                #     stdscr.addstr(row,col,ascii.ROGUE)
                # el
                if c == 1:
                    stdscr.addstr(row,col,ascii.FULL_BLOCK)
                    # print(r)
                elif c == 0:
                    stdscr.addstr(row,col,ascii.LIGHT_SHADE)
                else:
                    stdscr.addstr(row,col,c)
                index += 1
                col += 1
            row += 1
            col = 0
        stdscr.addstr((row),0,'Player pos: '+str(self.playerController.modelRef.getPosition())) # str(counter))
        row = 0
        # Changes go in to the screen buffer and only get
        # displayed after calling `refresh()` to update
        stdscr.refresh()

    def draw_stuff(self, stdscr):
        # screen = curses.initscr()
        self.render_field(stdscr)
        k = 0
        # Wait for next input
        screen = curses.initscr()
        k = screen.getch()

        # TODO: Key is being processed multiple times, fix this
        while (k != ord('q')):
            if k == curses.KEY_DOWN:
                self.playerController.move(PlayerController.SOUTH)
            elif k == curses.KEY_UP:
                self.playerController.move(PlayerController.NORTH)
            elif k == curses.KEY_RIGHT:
                self.playerController.move(PlayerController.EAST)
            elif k == curses.KEY_LEFT:
                self.playerController.move(PlayerController.WEST)
            self.levelModel.update()
            # levelView.set_player_pos(levelModel.playerModel.getPosition())
            # curses.wrapper(levelView.draw_stuff)
            screen.refresh()
        #     k = screen.getch()

