# import Vector
# import Enumeration
from src.header import TOY, HOLDER, DARK, MONSTER, TRAP, TUNNEL, STAIRS, HORWALL, VERTWALL, FLOOR, DOOR, HIDDEN
from src.itemvector import ItemVector
from src.potion import Potion
from src.rowcol import RowCol
from src.scroll import Scroll
from src.toy import Toy
from src.id import Id

class Level:
    def __init__(self, nrow, ncol, myself):
        self.myself = myself # Rogue type
        self.dummy  = None # Item
        self.level_men      = []
        self.level_toys     = []
        self.level_monsters = []
        self.level_traps    = []
        self.level_doors    = []
        self.map = [[]]     # 2D int array
        self.ncol = ncol       # width
        self.nrow = nrow       # height
        self.cur_level = 0  # level number
        self.max_level = 999
        self.my_level = 0
        self.foods = 0 # Higher levels get more food
        self.initialize()

    def initialize(self):
        # self.map = [self.nrow][self.ncol]
        for r in range(self.nrow):
            self.map.append([])
            for c in range(self.ncol):
                self.map[r].append(0)

        # for r in range(0,self.nrow):
        #     self.map[r] = []s
        #     for c in range(0,self.ncol): # c=0; c < ncol; c += 1):
        #         self.map[r][c] = 0

        self.level_monsters = ItemVector(6) # Start with a few monsters
        self.level_doors = ItemVector(8)    # , doors
        self.level_men = ItemVector()
        self.level_toys = ItemVector(6)
        self.level_traps = ItemVector(3)

    def mark(self, r,c):
        i = self.level_men.length
        while(i-1) >= 0:
            i -= 1
            self.level_men[i].view.mark(r,c)
    
    def get_char(self, row, col):
        if (row < 0 or row >= self.nrow or col < 0 or col >= self.ncol):
            return 0
        mask = self.map[row][col]
        if (0 != (mask & TOY)):
            # toy = self.level_toys.item_at(row, col)
            # return toy == null ? ';' : get_mask_char(toy.kind)
            pass
        # Not allowing hidden stairs
        if (0 != (mask & STAIRS)):
            return '%'
        if (0 != (mask & (TUNNEL|STAIRS|HORWALL|VERTWALL|FLOOR|DOOR))):
            if (0 == (mask & HIDDEN)):
                if (0 != (mask & TUNNEL)):
                    return '*'
                if (0 != (mask & HORWALL)):
                    return '-'
                if (0 != (mask & VERTWALL)):
                    return '|'
                if (0 != (mask & FLOOR)):
                    # return (mask & (HIDDEN|TRAP)) == TRAP ? '^' : '.'
                    if (mask & (HIDDEN|TRAP)) == TRAP:
                        return '^'
                    else:
                        return '.'
                if (0 != (mask & DOOR)):
                    return '+'
                # Hidden door:
                if (0 != (mask & TUNNEL)):
                    # return ' '; FOOP
                    return '$'
                if (self.col <= 0 or col >= self.ncol - 1):
                    return '|'
                if (0 != (self.map[row][col-1] & HORWALL)
                        or 0 != (self.map[row][col+1] & HORWALL)):
                    return '-'
                return '|'
        if (0 != (mask & TUNNEL)):
            return '$'
        return ' '

    def is_passable(self, row, col):
        if (row < self.MIN_ROW or row > (self.nrow - 2) or col < 0 or col > (self.ncol - 1)):
            return False
        if (0 != (self.map[row][col] & HIDDEN)):
            return 0 != (self.map[row][col] & TRAP)

    def can_turn(self, row, col):
        return 0 != (TUNNEL & self.map[row][col]) and self.is_passable(row, col)

    def can_move(self, row1, col1, row2, col2):
        if (self.is_passable(row2, col2) == False):
            return False
        if (row1 != row2 and col1 != col2):
            if (0 != ((self.map[row1][col1] | map[row2][col2]) & DOOR)):
                return False
            if (0 == self.map[row1][col2] or 0 == self.map[row2][col1]):
                return False
        return True

    def gr_row_col(self, mask, item):
        r = 0
        c = 0
        mask |= HOLDER|DARK
        ntry = 2400
        # do {
        #   if (--ntry > 0):
        #       r = myself.rand.get(MIN_ROW, nrow-2)
        #       c = myself.rand.get(ncol-1)
        #   else if (ntry == 0):
        #       r = nrow-2
        #       c = ncol-1
        #   else if (--c < 0):
        #       c = ncol-1
        #       if (--r < 0):
        #           return None
        # } while ( 0 == (self.map[r][c] & mask)
        #       || 0 != (self.map[r][c] & (~mask))
        #       || 0 == (self.map[r][c] & HOLDER)
        #       || (item != None && r == item.row && c == item.col))
        return RowCol(r,c)

    def plant_gold(self, row, col, gold):
        obj = Toy(self, id.GOLD)
        obj.quantity = gold
        obj.place_at(row, col, TOY)

    # Returns Scroll
    def gr_scroll(self):
        t = Scroll(self)
        t.kind = Id.gr_which_scroll(self.myself.rand)
        return t

    def gr_potion(self):
        t = Potion(self)
        t.king = Id.gr_which_potion(self.myself.rand)
        return t

    def gr_weapon(self, assign_wk):
        if (assign_wk < 0):
            assign_wk = self.rand.get(Id.id_weapons.length - 1)
        return Toy(self, Id.WEAPON|assign_wk)

    def gr_armor(self):
        return Toy(self, Id.ARMOR + self.rand.get(Id.id_armors.length-1))

    def gr_wand(self):
        return Toy(self, Id.WAND + self.rand.get(Id.id_wands.length-1))

    def get_food(self, force_ration):
        # if (self.rand.percent(80) )
        # return Toy(self, force_ration + self.rand.percent(80) ? Id.RATION : Id.FRUIT
        return -1

    def gr_toy(self):
        k = None
        if (self.foods < self.cur_level / 3):
            k = Id.FOOD
            foods += 1
        else:
            k = Id.gr_species(self.rand)
        if (k == Id.SCROLL):
            return self.gr_scroll()
        elif (k == Id.POTION):
            return self.gr_potion()
        elif (k == Id.WEAPON):
            return self.gr_weapon(-1)
        elif (k == Id.ARMOR):
            return self.gr_armor()
        elif (k == Id.WAND):
            return self.gr_wand()
        elif (k == Id.FOOD):
            return self.get_food(False)
        elif (k == Id.RING):
            return self.gr_ring()
        return None

    def wiztoy(self, man, ch):
        t = None
        max = 0
        # switch(ch):
