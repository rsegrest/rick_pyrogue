import curses
from ascii_helper import ASCII_Helper as ascii
# wrapper

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
            else:
                screen.addstr(row,col,ascii.LIGHT_SHADE)
                # print(c)
            index += 1
            col += 1
        row += 1
        col = 0
    screen.addstr((row),0,' ') # str(counter))
    row = 0
    # Changes go in to the screen buffer and only get
    # displayed after calling `refresh()` to update
    screen.refresh()

matrix = [[1,0,1,0,1,0,1,1],[1,1,1,0,1,0,1,1],[0,1,1,1,0,1,0,0]]
# matrix = [[1],[0],[0]]
# m = matrix
draw_stuff(matrix)
# Update the buffer, adding text at different locations
# screen.addstr(0, 0, "This string gets printed at position (0, 0)")
# screen.addstr(3, 1, "Try Russian text: Привет")  # Python 3 required for unicode
# screen.addstr(4, 4, "X")
# screen.addch(5, 5, "Y")
# index = 0
# row = 0
# col = 0
# for r in m:
#     for c in r:
#         if c == 1:
#             screen.addstr(row,col,ascii.FULL_BLOCK)
#             # print(r)
#         else:
#             screen.addstr(row,col,ascii.LIGHT_SHADE)
#             # print(c)
#         index += 1
#         col += 1
#     row += 1
#     col = 0
# row = 0

curses.napms(3000)
draw_stuff([[0],[0],[0]])

curses.napms(3000)
draw_stuff([[1],[0],[0]])

curses.napms(3000)
draw_stuff([[0],[0],[1]])
curses.curs_set(1)
curses.endwin()
