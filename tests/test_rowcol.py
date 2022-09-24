import sys

sys.path.append('..')

from src.rowcol import RowCol

def test_create_rowcol():
    rc = RowCol(1,1)
    assert rc != None
