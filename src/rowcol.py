class RowCol: 
        # row = None
        # col = None

        def __init__(self, r, c):
            self.row = r
            self.col = c

        def __str__(self):
            return '[' + str(self.row) + ' ' + str(self.col) + ']'


# rc = RowCol(2,2)
#print(str(rc))

