MIN_ROW = 1
AMULET_LEVEL = 26
LAST_map = 99

# Values for Level Map
TOY         =    0o01
MONSTER     =    0o02
STAIRS      =    0o04
HORWALL     =   0o010
VERTWALL    =   0o020
DOOR        =   0o040
FLOOR       =  0o0100
TUNNEL      =  0o0200
TRAP        =  0o0400
HIDDEN      = 0o01000
MAN         = 0o02000 # Rogue is here
HOLDER      = 0o04000 # May contain trap / toy / monster
DARK        =0o010000 # A Dark Place

DROPHERE    = (DOOR|FLOOR|TUNNEL|MAN|HOLDER|MONSTER)
SOMETHING   = 0o0777

