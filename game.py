import pyxel
pixtag = 15
pixsiz = 1

num_to_pixtag = {2:'wall', 4:'dirt', 12:'water', 15:'sand'}

class Map():    
    def update(self, x, y, tag):
        self.ele_x = x
        self.ele_y = y
        self.ele_tag = tag
        self.ele_f = 0

class App:
    def __init__(self):
        pyxel.init(256, 256, caption="SAND BOX")
        pyxel.mouse(True)

        #instance
        self.Maps = []
        
        pyxel.run(self.update, self.draw)

    def update(self):
        global pixtag
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        if pyxel.btnp(pyxel.KEY_R):
            pixtag = 15
            self.Maps.clear()

        if pyxel.btn(pyxel.MOUSE_LEFT_BUTTON) and 1 <= pyxel.mouse_x <= 199 and 1 <= pyxel.mouse_y <= 242:
            if pixsiz == 1:
                new_map = Map()
                new_map.update(pyxel.mouse_x, pyxel.mouse_y, pixtag)
                self.Maps.append(new_map)

            elif pixsiz == 2:
                new_map = Map()
                new_map.update(pyxel.mouse_x, pyxel.mouse_y, pixtag)
                self.Maps.append(new_map)

                new_map = Map()
                new_map.update(pyxel.mouse_x - 1, pyxel.mouse_y, pixtag)
                self.Maps.append(new_map)

                new_map = Map()
                new_map.update(pyxel.mouse_x, pyxel.mouse_y - 1, pixtag)
                self.Maps.append(new_map)

                new_map = Map()
                new_map.update(pyxel.mouse_x - 1, pyxel.mouse_y - 1, pixtag)
                self.Maps.append(new_map)

        element_count = len(self.Maps)
        for e in range(element_count):
            self.Maps[e].ele_f = self.Maps[e].ele_f + 1

            #一定フレームごとに落下
            if self.Maps[e].ele_f % 1 == 0:
                flg = 0
                for i in range(element_count):
                    if self.Maps[e].ele_x == self.Maps[i].ele_x and self.Maps[e].ele_y + 1 == self.Maps[i].ele_y:
                        flg = 1
                if flg == 0:        
                    if 1 <= self.Maps[e].ele_x <= 199 and 1 <= self.Maps[e].ele_y <= 241:   #描画可能領域範囲内か
                        self.Maps[e].ele_y = self.Maps[e].ele_y + 1
        
    def draw(self):
        pyxel.cls(0)
        self.flame()
        self.pallet()
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            self.pix_select()
        self.pix_tags()
        pyxel.text(10, 246, "HAVE FUN !", pyxel.frame_count % 16)
        pyxel.text(220, 236, "(Q)UIT", 7)
        pyxel.text(220, 246, "(R)ESET", 7)

        #描画
        for maps in self.Maps:
            pyxel.rect(maps.ele_x, maps.ele_y, 1, 1, maps.ele_tag)

    def flame(self):
        pyxel.line(0, 1, 0, 243, 1)#left line
        pyxel.line(200, 0, 200, 243, 1)#right line
        pyxel.line(0, 243, 200, 243, 1)#under line

    def pallet(self):
        pyxel.rect(215, 1, 25, 10, 12)#water
        pyxel.rect(215, 12, 25, 10, 15)#sand
        pyxel.rect(215, 23, 25, 10, 4)#dirt

        pyxel.rect(215, 200, 25, 10, 7)#1
        pyxel.rect(215, 212, 25, 10, 7)#2
        pyxel.text(222, 202, "1x1", 0)
        pyxel.text(222, 214, "2x2", 0)

    def pix_select(self):
        global pixtag
        if 215 <= pyxel.mouse_x <= 240 and 1 <= pyxel.mouse_y <= 11:
            pixtag = 12
        elif 215 <= pyxel.mouse_x <= 240 and 12 <= pyxel.mouse_y <= 22:
            pixtag = 15
        elif 215 <= pyxel.mouse_x <= 240 and 23 <= pyxel.mouse_y <= 33:
            pixtag = 4

        global pixsiz
        if 215 <= pyxel.mouse_x <= 240 and 200 <= pyxel.mouse_y <= 211:
            pixsiz = 1
        elif 215 <= pyxel.mouse_x <= 240 and 212 <= pyxel.mouse_y <= 222:
            pixsiz = 2

    def pix_tags(self):
        if pixtag == 12:
            pyxel.text(100, 246, "WATER", 12)
        elif pixtag == 15:
            pyxel.text(100, 246, "SAND", 15)
        elif pixtag == 4:
            pyxel.text(100, 246, "DIRT", 4)

        if pixsiz == 1:
            pyxel.text(160, 246, "size:1x1", 7)
        elif pixsiz == 2:
            pyxel.text(160, 246, "size:2x2", 7)

App()
