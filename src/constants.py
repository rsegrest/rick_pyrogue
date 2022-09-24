MIN_ROW = 1
AMULET_LEVEL = 26
LAST_map = 99

# Values for Level Map
TOY         =    01
MONSTER     =    02
STAIRS      =    04
HORWALL     =   010
VERTWALL    =   020
DOOR        =   040
FLOOR       =  0100
TUNNEL      =  0200
TRAP        =  0400
HIDDEN      = 01000
MAN         = 02000 # Rogue is here
HOLDER      = 04000 # May contain trap / toy / monster
DARK        =010000 # A Dark Place

DROPHERE    = (DOOR|FLOOR|TUNNEL|MAN|HOLDER|MONSTER)
SOMETHING   = 0777

