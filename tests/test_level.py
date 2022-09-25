from src.level import Level
from src.rogue import Rogue

def test_level():
    level = Level(3,3,Rogue())
    assert level != None

