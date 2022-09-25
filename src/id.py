# String Tokenizer
# Event
import math
from typing import TypeVar, Type, NewType, List
# IdT = TypeVar('IdT', bound='Id')
IdT = TypeVar("IdT")
Ids = NewType('Ids', List[IdT])

class Id:
    ARMOR =     0x00100
    WEAPON =    0x00200
    SCROLL =    0x00400
    POTION =    0x00800
    GOLD =      0x01000
    FOOD =      0x02000
    WAND =      0x04000
    RING =      0x08000
    AMULET =    0x10000
    ALL_TOYS =  0x1FF00
    
    LEATHER =   0+ARMOR
    RINGMAIL =  1+ARMOR
    SCALE =     2+ARMOR
    CHAIN =     3+ARMOR
    BANDED =    4+ARMOR
    SPLINT =    5+ARMOR
    PLATE =     6+ARMOR
    ARMORS =    7+ARMOR
    
    BOW =               0+WEAPON
    DART =              1+WEAPON
    ARROW =             2+WEAPON
    DAGGER =            3+WEAPON
    SHURIKEN =          4+WEAPON
    MACE =              5+WEAPON
    LONG_SWORD =        6+WEAPON
    TWO_HANDED_SWORD =  7+WEAPON
    WEAPONS =           8

    PROTECT_ARMOR =     0+SCROLL
    HOLD_MONSTER =      1+SCROLL
    ENCH_WEAPON =       2+SCROLL
    ENCH_ARMOR =        3+SCROLL
    IDENTIFY =          4+SCROLL
    TELEPORT =          5+SCROLL
    SLEEP =             6+SCROLL
    SCARE_MONSTER =     7+SCROLL
    REMOVE_CURSE =      8+SCROLL
    CREATE_MONSTER =    9+SCROLL
    AGGRAVATE_MONSTER = 10+SCROLL
    MAGIC_MAPPING =     11+SCROLL
    CON_MON =           12+SCROLL
    SCROLLS =           13+SCROLL
    
    INCREASE_STRENGTH = 0+POTION
    RESTORE_STRENGTH =  1+POTION
    HEALING =           2+POTION
    EXTRA_HEALING =     3+POTION
    POISON =            4+POTION
    RAISE_LEVEL=        5+POTION
    BLINDNESS=          6+POTION
    HALLUCINATION=      7+POTION
    DETECT_MONSTER=     8+POTION
    DETECT_TOYS=        9+POTION
    CONFUSION=          10+POTION
    LEVITATION=         11+POTION
    HASTE_SELF=         12+POTION
    SEE_INVISIBLE=      13+POTION
    POTIONS=            14+POTION

    TELE_AWAY=          0+WAND
    SLOW_MONSTER=       1+WAND
    INVISIBILITY=       2+WAND
    POLYMORPH=          3+WAND
    HASTE_MONSTER=      4+WAND
    MAGIC_MISSILE=      5+WAND
    CANCELLATION=       6+WAND
    DO_NOTHING=         7+WAND
    DRAIN_LIFE=         8+WAND
    COLD=               9+WAND
    FIRE=               10+WAND
    WANDS=              11+WAND

    STEALTH=            0+RING
    R_TELEPORT=         1+RING
    REGENERATION=       2+RING
    SLOW_DIGEST=        3+RING
    ADD_STRENGTH=       4+RING
    SUSTAIN_STRENGTH=   5+RING
    DEXTERITY=          6+RING
    ADORNMENT=          7+RING
    R_SEE_INVISIBLE=    8+RING
    MAINTAIN_ARMOR=     9+RING
    SEARCHING=          10+RING
    RINGS=              11+RING

    RATION=             0+FOOD
    FRUIT=              1+FOOD

    NOT_USED        =   0o0000
    BEING_WIELDED   =   0o0001
    BEING_WORN	    =   0o0002
    ON_LEFT_HAND    =   0o0004
    ON_RIGHT_HAND   =   0o0010
    ON_EITHER_HAND  =   0o0014
    BEING_USED      =   0o0017

    UNIDENTIFIED=   0
    IDENTIFIED=     1
    CALLED=         2

    UPWARD =        0
    UPRIGHT =       1
    RIGHT =         2
    DOWNRIGHT =     3
    DOWN =          4
    DOWNLEFT =      5
    LEFT =          6
    UPLEFT =        7
    DIRS =          8
    
    xtab = [1,1,0,-1,-1,-1,0,1,0]
    ytab = [0,1,1,1,0,-1,-1,-1,0]
    potionsList = [
        "100", "blue ", "of increase strength",
        "250", "red ",		"of restore strength ",
        "100", "green ",	"of healing ",
        "200", "grey ",		"of extra healing ",
        "10", "brown ",	"of poison ",
        "300", "clear ",	"of raise level ",
        "10", "pink ",		"of blindness ",
        "25", "white ",	"of hallucination ",
        "100", "purple ",	"of detect monster ",
        "100", "black ",	"of detect things ",
        "10", "yellow ",	"of confusion ",
        "80", "plaid ",	"of levitation ",
        "150", "burgundy ",	"of haste self ",
        "145", "beige ",	"of see invisible "
    ]
    scrollsList = [
        "505", "", "of protect armor ",
        "200", "", "of hold monster ",
        "235", "", "of enchant weapon ",
        "235", "", "of enchant armor ",
        "175", "", "of identify ",
        "190", "", "of teleportation ",
        "25", "", "of sleep ",
        "610", "", "of scare monster ",
        "210", "", "of remove curse ",
        "80", "", "of create monster ",
        "25", "", "of aggravate monster ",
        "180", "", "of magic mapping ",
        "90", "", "of confuse monster "
    ]
    syllables = [
        "blech ","foo ","barf ","rech ","bar ",
		"blech ","quo ","bloto ","oh ","caca ",
		"blorp ","erp ","festr ","rot ","slie ",
		"snorf ","iky ","yuky ","ooze ","ah ",
		"bahl ","zep ","druhl ","flem ","behil ",
		"arek ","mep ","zihr ","grit ","kona ",
		"kini ","ichi ","tims ","ogr ","oo ",
		"ighr ","coph ","swerr ","mihln ","poxi "
    ]
    weaponsList = [
        "150", "short bow ", "",
        "8", "darts ", "",
        "15", "arrows ", "",
        "27", "daggers ", "",
        "35", "shurikens ", "",
        "360", "mace ", "",
        "470", "long sword ", "",
        "580", "two-handed sword ", ""
    ]
    armorsList = [
        "300", "leather armor ", "",
        "300", "ring mail ", "",
        "400", "scale mail ", "",
        "500", "chain mail ", "",
        "600", "banded mail ", "",
        "600", "splint mail ", "",
        "700", "plate mail ", ""
    ]
    wandsList = [
        "25", "", "of teleport away ",
        "50", "", "of slow monster ",
        "8", "", "of invisibility ",
        "55", "", "of polymorph ",
        "2", "", "of haste monster ",
        "20", "", "of magic missile ",
        "20", "", "of cancellation ",
        "0", "", "of do nothing ",
        "35", "", "of drain life ",
        "20", "", "of cold ",
        "20", "", "of fire "
    ]

    ringsList = [
        "250", "", "of stealth ",
        "100", "", "of teleportation ",
        "255", "", "of regeneration ",
        "295", "", "of slow digestion ",
        "200", "", "of add strength ",
        "250", "", "of sustain strength ",
        "250", "", "of dexterity ",
        "25", "", "of adornment ",
        "300", "", "of see invisible ",
        "290", "", "of maintain armor ",
        "270", "", "of searching "
    ]
    
    wand_materials = [
        "steel ","bronze ","gold ","silver ","copper ",
        "nickel ","cobalt ","tin ","iron ","magnesium ",
        "chrome ","carbon ","platinum ","silicon ","titanium ",
        "teak ","oak ","cherry ","birch ","pine ",
        "cedar ","redwood ","balsa ","ivory ","walnut ",
        "maple ","mahogany ","elm ","palm ","wooden "
    ]
	# static boolean is_wood[]= new boolean[wand_materials.length];
	# static {
	# 	boolean wood= false;
	# 	for(int k= 0; k<is_wood.length; k++){
	# 		if(wand_materials[k].compareTo("teak")==0)
	# 			wood= true;
	# 		is_wood[k]= wood;
	# 	}
	# }
    gems = [
        "diamond ","stibotantalite ","lapi-lazuli ","ruby ","emerald ",
        "sapphire ","amethyst ","quartz ","tiger-eye ","opal ",
        "agate ","turquoise ","pearl ","garnet "
    ]
    def __init__(self):
        self.value = None
        self.title = None
        self.real = None
        self.id_status = None
    
    def mix_colors(self, rand):
        # for(int j= id_potions.length; --j>1;){
		# 	int k= rand.get(j-1);
		# 	String t= id_potions[j].title;
		# 	id_potions[j].title= id_potions[k].title;
		# 	id_potions[k].title= t;
		# }
        return -1
    
    def make_scroll_titles(self, rand):
        # // Also name the wands and rings
        # for(int i= 0; i < id_scrolls.length; i++){
        # 	int sylls= rand.get(2, 5);
        # 	String ti= "'";
        # 	for(int j= 0; j < sylls; j++){
        # 		int s= rand.get(1, syllables.length-1);
        # 		ti= ti.concat(syllables[s]);
        # 	}
        # 	id_scrolls[i].title= ti.concat("' ");
        # }
        # int perm[]= rand.permute(wand_materials.length);
        # for(int i= 0; i<id_wands.length; i++)
        # 	id_wands[i].title= wand_materials[perm[i]];

        # perm= rand.permute(gems.length);
        # for(int i= 0; i<id_rings.length; i++)
        # 	id_rings[i].title= gems[perm[i]];
        return -1
    
    def is_direction(self, c):
        # if ((c == Event.LEFT) or (c == 'h')):
        #     return LEFT
        # if ((c == Event.DOWN) or (c == 'j')):
        #     return DOWN
        # if ((c == Event.UP) or (c == 'k')):
        #     return UPWARD
        # if ((c == Event.RIGHT) or (c == 'l')):
        #     return RIGHT
        # if ((c == Event.HOME) or (c == 'y')):
        #     return UPLEFT
        # if ((c == Event.PGUP) or (c == 'u')):
        #     return UPRIGHT
        # if ((c == Event.PGDN) or (c == 'n')):
        #     return DOWNRIGHT
        # if (c=='\033'):
        #     return -1
        return -2

    def get_dir(self, srow, scol, drow, dcol):
        if (srow > drow):
            if (scol > dcol):
                return self.UPLEFT
            elif (scol < dcol):
                return self.UPRIGHT
            else:
                return self.UPWARD
        if (srow < drow):
            if (scol > dcol):
                return self.DOWNLEFT
            elif (scol < dcol):
                return self.DOWNRIGHT
            else:
                return self.DOWN
        if scol < dcol:
            return self.RIGHT
        return self.LEFT
    
    # def foo(self, bar: Type[MyClassT]) -> MyClassT:
    #     return MyClass(self.attr_a + bar.attr_a)
    # , IdT: Type[IdT]
    @staticmethod
    def idlist(mylist, status, bar: Type[IdT]) -> List[IdT]:
        # n = len(mylist) / 3
        # i = 0
        # n_int = math.floor(n)
        # ids = []
        # for k in range(n_int):
        #     # create new id
        #     # ids.append(bar.__init__())
        #     new_id = bar.__init__()
        #     ids.append(new_id)
        #     ids[k]['value'] = int(mylist[i])
        #     i += 1
        #     ids[k]['title'] = mylist[i]
        #     i += 1
        #     ids[k]['real'] = mylist[i]
        #     ids[k]['id_status'] = status
        # return ids
        return []
    
    @staticmethod
    def list_items():
        Id.id_potions = Id.idlist(Id.potionsList, 0, 'Id')
        Id.id_scrolls = Id.idlist(Id.scrollsList, 0, 'Id')
        Id.id_weapons = Id.idlist(Id.weaponsList, 0, 'Id')
        Id.id_armors = Id.idlist(Id.armorsList, 0, 'Id')
        Id.id_wands = Id.idlist(Id.wandsList, 0, 'Id')
        Id.id_rings = Id.idlist(Id.ringsList, 0, 'Id')
        

    id_weapons = idlist.__func__(weaponsList, 0, 'Id')
    id_scrolls = idlist.__func__(scrollsList, 0, 'Id')
    id_potions = idlist.__func__(potionsList, 0, 'Id')
    
    id_armors = idlist.__func__(armorsList, 0, 'Id')
    id_wands = idlist.__func__(wandsList, 0, 'Id')
    id_rings = idlist.__func__(ringsList, 0, 'Id')

    @staticmethod
    def is_vowel(ch):
        if (ch < 'a'):
            ch += 32
        return ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'

    @staticmethod
    def get_mask_char(mask):
        switcher = mask&Id.ALL_TOYS
        if (switcher == Id.POTION):
            return '!'
        if (switcher == Id.SCROLL):
            return '?'
        if (switcher == Id.WAND):
            return '/'
        if (switcher == Id.RING):
            return '='
        if (switcher == Id.ARMOR):
            return ']'
        if (switcher == Id.WEAPON):
            return ')'
        if (switcher == Id.GOLD):
            return '$'
        if (switcher == Id.FOOD):
            return '%'
        if (switcher == Id.AMULET):
            return ','
        else:
            return '~' # unknown, something is wrong
    
    @staticmethod
    def get_id_table(kind):
        switcher = kind&Id.ALL_TOYS
        if (switcher == Id.SCROLL):
            return Id.id_scrolls
        if (switcher == Id.POTION):
            return Id.id_potions
        if (switcher == Id.WAND):
            return Id.id_wands
        if (switcher == Id.RING):
            return Id.id_rings 
        