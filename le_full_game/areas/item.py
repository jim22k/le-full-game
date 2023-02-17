from .space import Space


class Item(Space):
    def __init__(self, name, text, torch, sword, magic, amulet, fairy, dark, wood, pix, axe, bean):
        super().__init__()
        self.name = name
        self.text = text
        self.torch = torch
        self.sword = sword
        self.magic = magic
        self.amulet = amulet
        self.fairy = fairy
        self.dark = dark
        self.bean = bean
        self.wood = wood
        self.pix = pix
        self.axe = axe
    
    def walked_in(self, gs):
        if gs.past_coords == (0,-1):
            if gs.add == 'h':
                self.print('wall in the way')
                gs.coord = gs.past_coords
                return
        if self.dark == 1:
            if gs.player_fire != 1:
                self.print('It is too dark to see')
                return
        
        if self.bean == 0:
            self.print(self.text)
            self.bean = 1
        else:
            self.print(self.name)
    
        if self.wood == 1:
            gs.has_wood = 1
        if self.torch == 1:
            gs.player_fire = 1
        if self.axe == 1:
            gs.player_chop = 1
        if self.magic == 1:
            gs.magic = 1
        if self.amulet == 1:
            gs.amulet = 1
        if self.fairy == 1:
            gs.fairy = 1
        if self.pix == 1:
            gs.pix = 1
        if self.sword == 1:
            gs.sword = 1
