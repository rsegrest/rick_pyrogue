class ItemVector:
    def __init__(self, n=None):
        pass
    def relevel(self, level):
        # Enumeration e = elements()
        # while (e.hasMoreElements()):
        #     Item item = (Item) e.nextElement()
        pass
    def item_at(self, row, col):
        i = self.length
        # while i <= 0:
        while (i - 1) >= 0:
            i -= 1
            p = self[i]
            if (p.row == row and p.col == col):
                return p
        return None
    def inventory(self,mask,msg,ask):
        i = self.length
        descs = ['']
        descs[0] = '--'
        
        if (i == 0):
            msg.message('Your pack is empty')
            return '\033'
        n = 0
        e = self.elements()
        while(e.hasMoreElements()):
            obj = e.nextElement()
            if (0 != (obj.kind & mask)):
                # descs[n] = item.description()
                n += 1
        if (n > 0):
            descs = [] # new String[n]
            n = 0
            while(e.hasMoreElements()):
                obj = e.nextElement()
                if (0 != (obj.kind & mask)):
                    k = n
                    if obj.ichar >= 'a' and obj.ichar <= 'z':
                        k = obj.ichar
                    n+=1
                    descs[n] = self.single_inv(k)
                    # and obj.ichar or obj.ichar.lower()
        if (n == 0):
            descs = ['']
            descs[0] = '--nothing appropriate--'
        return msg.rightlist(descs, ask)
    def single_inv(self, ch):
        if (ch < 'a'):
            ch += 'a'
        e = self.elements()
        obj = None
        while(e.hasMoreElements()):
            obj = e.nextElement()
            if (obj.ichar == ch):
                break
        if (obj == None):
            return ""
        sep = ") "
        if (0 != (obj.kind & Id.ARMOR) and obj.is_protected):
            sep = "} "
        return " " + obj.ichar + sep + obj.get_desc()

    def mask_pack(self, mask):
        i = self.length
        while (i-1) >= 0:
            i -= 1
            t = self[i]
            if (0 != (t.kind & mask)):
                return True
        return False
    
    def next_avail_ichar(self):
        i = None
        ichars = []
        for i in range(26):
            ichars.append(None)
        i = self.length
        while (i-1) >= 0:
            i -= 1
            obj = self[i]
            k = obj.ichar - 'a'
            if (k >= 0 and k < 26):
                ichars[k] = True
        for i in range(26):
            if (ichars[i] == None):
                return chr(i + 'a')
        return '?'
    
    def uncurse_all(self):
        e = self.elements()
        while(e.hasMoreElements()):
            obj = e.nextElement()
            obj.is_cursed = False