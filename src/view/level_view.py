import curses
from events import Events
from src.ascii_helper import ASCII_Helper as ascii


class LevelView:
    def __init__(self, initial_layout):
        self.events = Events()
        self.layout = initial_layout
        self.userInput = []
        self.playerPos = []

    def set_player_pos(self, pos):
        self.playerPos = pos

    def get_user_input(self):
        return self.userInput

    def consume_user_input(self):
        input = self.userInput
        self.userInput = []
        return input

    def clear_user_input(self):
        self.userInput = []

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
        # Controller should set player position
        # stdscr.addstr((row),0,'Player pos: '+str(self.playerController.modelRef.getPosition())) # str(counter))
        row = 0
        # Changes go in to the screen buffer and only get
        # displayed after calling `refresh()` to update
        stdscr.refresh()
    
    @staticmethod
    def key_event(key):
        print("the key %s was pressed" % key)
        return key

    def draw_stuff(self, stdscr):
        # screen = curses.initscr()
        self.render_field(stdscr)
        k = 0
        # Wait for next input
        screen = curses.initscr()
        k = screen.getch()

        # TODO: View should just record key presses, and create signals for the controller
        # TODO: Key is being processed multiple times, fix this
        while (k != ord('q')):
            if k == curses.KEY_DOWN:
                # self.playerController.move(PlayerController.SOUTH)
                self.userInput = [curses.KEY_DOWN]
                self.events.key_event(curses.KEY_DOWN)
            elif k == curses.KEY_UP:
                self.playerController = [curses.KEY_UP]
                self.events.key_event(curses.KEY_UP)
            elif k == curses.KEY_RIGHT:
                self.playerController = [curses.KEY_RIGHT]
                self.events.key_event(curses.KEY_RIGHT)
            elif k == curses.KEY_LEFT:
                self.playerController = [curses.KEY_LEFT]
                self.events.key_event(curses.KEY_LEFT)
            # self.levelModel.update() # move this to the controller

            screen.refresh()

