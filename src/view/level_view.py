import curses
from src.ascii_helper import ASCII_Helper as ascii
# wrapper

class LevelView:
    @staticmethod
    def draw_stuff(m):
        screen = curses.initscr()
        screen.clear()
        curses.curs_set(0)
        counter = 0
        index = 0
        row = 0
        col = 0
        for r in m:
            for c in r:
                counter += 1
                if c == 1:
                    screen.addstr(row,col,ascii.FULL_BLOCK)
                    # print(r)
                elif c == 0:
                    screen.addstr(row,col,ascii.LIGHT_SHADE)
                else:
                    screen.addstr(row,col,c)
                index += 1
                col += 1
            row += 1
            col = 0
        screen.addstr((row),0,' ') # str(counter))
        row = 0
        # Changes go in to the screen buffer and only get
        # displayed after calling `refresh()` to update
        screen.refresh()
