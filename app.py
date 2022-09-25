from src.rowcol import RowCol
from src.item import Item
from src.randomx import RandomX

if __name__=='__main__':
    rc = RowCol(10,12)
    i = Item(rc)
    # print(rc)
    # print('Item: ' + str(i))
    #rand = RandomX(10)
    rand = RandomX(10)
    pct = rand.percent(5)
    print(pct)
