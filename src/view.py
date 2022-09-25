import curses

class View:

    cmap = [curses.COLOR_BLACK] * 8
    # cmap[0]= Color.lightGray;
    # cmap[1]= Color.gray;
    cmap[2]= curses.COLOR_BLACK
    cmap[3]= curses.COLOR_WHITE
    cmap[4]= curses.COLOR_RED
    cmap[5]= curses.COLOR_YELLOW
    # cmap[6]= new Color(128,0,0);	// Dark red
    cmap[7]= curses.COLOR_GREEN

    def __init__(self, myself, pointsize, nrow, ncol):
        self.myself = myself
        self.pointsize = pointsize
        self.nrow = nrow
        self.ncol = ncol
        # self.terminal = [[' ' for x in range(ncol)] for y in range(nrow)]
        self.buffer = None # char[][]
        self.line_dirty = None  # boolean[]
        self.cw = None          # int (character width)
        self.ch = None          # int (character height)
        self.ca = None          # int (character ascent)
        self.lead = None        # font leading
        self.ffixed = None      # Font
        self.fm = None          # FontMetrics
        self.man = None         # "From whose point of view this is"

        for k in range(self.nrow):
            self.line_dirty[k] = False
            for c in range(self.ncol):
                self.terminal[k][c] = ' '
        
        # Dimension d = preferredSize()
        # resize(d)
        # requestFocus()
    
    def preferredSize(self):
        d = self.size()
        self.pointsize += 1
        if d.height > 0:
            self.pointsize += self.pointsize/2
        # do:
        #     self.pointsize += 1
        #     self.ffixed = Font("Monospaced", Font.PLAIN, self.pointsize)
        #     self.fm = self.getfontmetrics(self.ffixed)
        #     self.cw = self.fm.charwidth(' ')
        #     self.ch = self.fm.height
        #     self.ca = self.fm.ascent
        #     self.lead = self.fm.leading
        #     d.width = self.cw * self.ncol
        #     d.height = self.ch * self.nrow
        # while d.width < 200 or d.height < 200
        return 'stub'
    
    def in_sight(self, row, col):
        return self.man.can_see(row, col)
    
    

