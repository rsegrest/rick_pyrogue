import datetime
import gc
import numpy as np

from multiprocessing.sharedctypes import synchronized
from threading import Thread
from src.id import Id
from src.view import View
from src.man import Man
from src.nineroom import NineRoom

class Rogue:
    def __init__(self):
        self.gamer = None       # Thread
        self.level = None       # Level
        self.view_list = None   # Vector
        self.flashers = None    # Vector
        self.rand = None        # RandomX
        self.keybuf = ""        # String
        self.starttime = None   # long

        self.pointsize = 12
        self.scorepagename = ''
        self.interrupted = False

        self.newlevel = True
        # try {
        # 	pointsize= Integer.parseInt(getParameter("pointsize"));
        # }catch (NumberFormatException e){
        # 	pointsize= 12;
        # }
        # rand= new Randomx((int)System.currentTimeMillis());
        # try {
        # 	int i= Integer.parseInt(getParameter("srand"));
        # 	rand= new Randomx(i);
        # }catch (NumberFormatException e){
        # }
        # scorepagename= getParameter("score");
        # setBackground(Color.black);
        # Monster m= new Monster();	// Force static definitions
    
    def start(self):
        self.gamer = Thread()
        self.gamer.start()
        self.repaint(30)
    
    def stop(self):
        if (self.gamer != None):
            self.gamer.stop()
        self.gamer = None

    def begin_game(self):
        view = None
        Id.list_items()
        if (len(self.view_list) == 0):
            self.add(View(self, self.pointsize, 25, 80))
            self.view_list.append(view)
            self.man = Man(self, view)
        else:
            self.view = self.view_list[0]
            man = self.view.man
            # oldop = man != None ? man.option : None
            oldop = None
            if (man != None):
                oldop = man.option
            
            self.view.empty()
            self.view.man = man = Man(self, self.view)
            self.man.option = oldop
        gc.collect() # Garbage Collection
        self.view.requestFocus()
        Id.mix_colors(self.rand)
        Id.make_scroll_titles(self.rand)
        self.level.cur_level = 0
        self.level.max_level = 0
        d = datetime()
        self.starttime = d.getTime()
    def run(self):
        man = None
        e = None
        self.gamer.setPriority(Thread.MIN_PRIORITY)
        while(True):
            if(self.newlevel):
                if(len(self.view_list)==0):
                    self.begin_game()
                self.interrupted = False
                self.level = NineRoom(25,80,self)
                self.level.put_monsters()
                e = self.view_list.elements()
                while(e.hasMoreElements()):
                    v = e.nextElement()
                    man = v.man
                    man.level = self.level

                    if (self.man.pack == None):
                        self.man.player_init()
                    if (not self.man.has_amulet() and self.level.cur_level >= Level.AMULET_LEVEL):
                        pt = self.level.gr_row_col(Level.FLOOR|Level.TUNNEL, None)
                        if (pt != None):
                            amulet = Toy(self.level, Id.AMULET)
                            amulet.place_at(pt.row, pt.col, Level.TOY)
                    v.level = self.level
                    v.empty()
                    v.man.pack.relevel(self.level)
                    self.level.put_player(v.man)
                self.newlevel = False
            e = self.view_list.elements()
            while(e.hasMoreElements()):
                v = e.nextElement()
                v.man.init_seen()
                v.man.print_stat()
                v.refresh
            self.repaint()
            man = self.view_list.elementAt(0).man
            man.play_level()
            if (man.game_over):
                self.md_slurp()
                self.begin_game()
            self.newlevel = True

    def paint(self, g):
        e = None
        y = 0
        e = self.view_list.elements()
        while(e.hasMoreElements()):
            v = e.nextElement()
            s = self.size()
            d = self.v.size()
            v.move((s.width - d.width) / 2, y+v.ch)
            v.repaint()
            y += d.height+2*v.ch
    
    def mouseDown(self, evt, x, y):
        return True
    
    def mouseUp(self, evt, x, y):
        return True
    
    def keyDown(self, evt, key):
        if (key == '\033'):
            self.interrupted = True
        if (not self.gamer.isAlive()):
            if (key == ' '):
                self.start()
        else:
            self.keybuf = self.keybuf+(chr(key))
        self.notify()
        return True
    
    def md_sleep(self, mseconds):
        if (mseconds>0):
            # try:
            self.wait(mseconds)
            # except InterruptedException e:
                # pass
        self.keybuf = ""
    
    def md_slurp(self):
        self.keybuf = ""

    def md_getchar(self):
        while(self.keybuf == None or len(self.keybuf)==0):
            try:
                self.wait()
            except Exception as e:
                self.interrupted = True
                return '\033'
    
    def rgetchar(self):
        return self.md_getchar()
    
    def wait_for_ack(self):
        c = None
        # do: c = self.rgetchar()
        # while: (c != '\033' and c != ' ' and c != '\r' and c != '\
        return None
    
    def flashadd(self, row, col, color):
        ia = [0] * 3
        ia[0] = row
        ia[1] = col
        ia[2] = color
        self.flashers.addElement(ia)
    
    def xflash(self):
        if len(self.flashers) > 0:
            bseen = False
            e = self.view_list.elements()
            chsave = np.array(len(self.flashers))

            while(e.hasMoreElements()):
                v = e.nextElement()
                f = self.flashers.elements()
                vseen = False
                while(f.hasMoreElements()):
                    ia = f.nextElement()
                    if v.in_sight(ia[0], ia[1]):
                        ch = v.terminal[ia[0]][ia[1]]
                        chsave.addElement()
                        ch &= 255
                        if (ch == '.'):
                            ch = '*'
                        ch = (ch&255) | (ia[2])
                        v.addch(ia[0], ia[1], (chr(ch)))
                        vseen = True
                if vseen:
                    v.refresh()
                    bseen = True
                    self.md_self(self.mseconds)
            e = self.view_list.elements()
            # if bseen:
            #     while(e.hasMoreElements()):
            #         v = e.nextElement()
            #         f = self.flashers.elements()
            #         c = self.chsave.elements()

            #         while(f.hasMoreElements()):
            #             ia = f.nextElement()
            #             if v.in_sight(ia[0], ia[1]):
            #                 v.addch(ia[0], ia[1], (chr(chsave.elementAt(0))))
            #                 chsave.removeElementAt(0)
            #             v.mark(ia[0], ia[1])
            self.flashers = np
    def vflash(self, r, c, ch):
        bseen = False
        e = self.view_list.elements()
        while(e.hasMoreElements()):
            v = e.nextElement()
            if v.in_sight(r, c):
                bseen = True
                v.addch(r, c, ch)
        if(bseen):
            self.refresh()
            self.md_sleep(50)
            ch = self.level.get_char(r, c)
            e = self.view_list.elements()
            while(e.hasMoreElements()):
                v = e.nextElement()
                v.addch(r,c,ch)

    def tell(self,p,s,bintr):
        e = self.view_list.elements()
        while(e.hasMoreElements()):
            v = e.nextElement()
            if(v.man==p):
                ss = self.whoify(p,s)
                v.msg.message(ss, bintr)
        self.xflash()
    
    def describe(self,  rc, s, bintr):
        e = self.view_list.elements()
        while(e.hasMoreElements()):
            v = e.nextElement()
            if(v.in_sight(rc.row, rc.col)):
                ss = self.whoify(v.man, s)
                v.msg.message(s, bintr)
                return True
        self.xflash()
        return True
    
    def check_message(self, p):
        e = self.view_list.elements()
        while(e.hasMoreElements()):
            v = e.nextElement()
            if (v.man == p):
                v.msg.check_message()

    def refresh(self):
        e = self.view_list.elements()
        while(e.hasMoreElements):
            v = e.nextElements()
            v.refresh()
    
    def vset(self,r,c):
        e = self.view_list.elements()
        while(e.hasMoreElements()):
            v = e.nextElement()
            ch = self.v.charat(r,c)
            v.addch(r,c,ch)

    def mark(self, r, c):
        e = self.view_list.elements()
        while(e.hasMoreElements()):
            v = e.nextElement()
            v.mark(r,c)
    
    def markall(self):
        e = self.view_list.elements()
        while(e.hasMoreElements()):
            v = e.nextElement()
            v.markall()

    def whoify(self, p, src):
        pass
        # dst = ""
        # i = 0
        # j = 0
        # try:
        #     while (j = src.indexOf('@', i)) >= 0:
        #         dst += src.substring(i, j)
        #         j += 1
        #         hasverb = src.charAt(j) == '>'
        #         i = j+1
        #         if (hasverb):
        #             j = src.indexOf('+', i)
        #         else:
        #             j = src.indexOf('>', i)
        #         byou = False
        #         name = src.substring(i, j)
        #         if (name.equals(p.name())):
        #             dst += "you"
        #             byou = True
        #         else:
        #             dst += "the " + name
        #         if (hasverb):
        #             i = j + 1
        #             dst += " "
        #             j = src.indexOf('+', i)
        #             if (byou):
        #                 dst += src.substring(i, j)
        #                 i = src.indexOf('<', j)
        #             else:
        #                 i = src.indexOf('<', j)
        #                 dst += src.substring(j+1, i)
        #         else:
        #             i = j
        #         i += 1
        # except Exception as e:
        #     print("whoify error on " + p.name())
        #     print(src+"\n"+dst)
        # dst += src.substring(i)
        # return dst


