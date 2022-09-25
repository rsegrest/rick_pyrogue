from src.rowcol import RowCol
from src.header import TOY, MONSTER, MAN, TRAP, DOOR

class Item(RowCol):
    def __init__(self, level = 1, r = 1, c = 1):
        super().__init__(r,c)
        self.ichar = '?'
        self.level = level
        # self.row = r
        # self.col = c

    def __str__(self):
        return '[ichar:' + str(self.ichar) + ' Level:' + str(self.level) + '; Row: ' + str(self.row) + ', Col:'+str(self.col) + ']'

    def place_at(self,r,c,what):
        list = None
        if (what == TOY):
            list = self.level.level_toys
        elif (what == MONSTER):
            list = self.level.level_monsters
        elif (what == MAN):
            list = self.level.level_men
        elif (what == TRAP):
            list = self.level.level_traps
        elif (what == DOOR):
            list = self.level.level_traps
        
        if (list != None):
            row = r
            col = c
            if (list.contains(self)):
                self.level.mark(row,col)
                self.level.map[row][col] &= ~what
            elif (r >= 0):
                list.append(self)
            
        if (r>0):
            self.level.mark(r,c)
            self.level.map[r][c] |= what
        elif (list != None):
            list.remove(self)


