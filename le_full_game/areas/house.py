from .space import regions, Space, Transition, Wall
from .item import Item


class Stairs(Space):
    def __init__(self,nad,ncords,name,text):
        super().__init__()
        self.nad = nad
        self.ncords = ncords
        self.name = name
        self.text = text

    def walked_in(self, gs):
        if gs.past_coords == (0,1):
            self.print('wall in the way')
            gs.coord = gs.past_coords
        else:
            gs.add = self.nad
            gs.coord = self.ncords
            self.print(self.text)


class Room(Space):
    def __init__ (self,mn,ms,me,mw,text,name,bean):
        super().__init__()
        self.me = me
        self.ms = ms
        self.mn = mn
        self.mw = mw
        self.text = text
        self.name = name
        self.bean = bean

    def walked_in(self, gs):
        if self.me == gs.past_coords:
            gs.coord = gs.past_coords
            self.print('wall in the way')
            return
        if self.mn == gs.past_coords:
            gs.coord = gs.past_coords
            self.print('wall in the way')
            return
        if self.ms == gs.past_coords:
            gs.coord = gs.past_coords
            self.print('wall in the way')
            return
        if self.mw == gs.past_coords:
            gs.coord = gs.past_coords
            self.print('wall in the way')
            return
        if self.bean == 1:
            self.print(self.name)
        else:
            self.print(self.text)


regions["h"] = h = {}

h[-2, 1] = Wall()
h[-2, 0] = Wall()
h[-2, -1] = Wall()
h[-1, 2] = Wall()
h[-1, 1] = Stairs('attic',(0,2),'stairs','you walk up the stairs into the attic')
h[-1, 0] = Room(0,0,0,0,'A large staircase to the north leads upwards','staircase',0)
h[-1, -1] = Item('Workshop','''You are in a workshop, a large heavyset table sits in the center of the room. On the table is a note saying "Cannot find my axe, probably left it in the forest to the south/east." A torch hangs on the wall, you pick it up.
###############################
#  (\                         #
#  .'.   You got the torch    #
#  | |                        #
#  | |   with this you can    #
#  | |   see in dark places   #
#  |_|                        #
###############################                                 ''',1,0,0,0,0,0,0,0,0,0)
h[-1, -2] = Wall()
h[0, 2] = Wall()
h[0, 1] = Room(0,0,0,(-1,1),'You are in a room with a window looking out to the north over a large clearing, you can see a rushing river through a gap in the trees','window room',0)
h[0, 0] = Room(0,0,0,0,'You are in a living room. A red carpet is surounded by heavyset mahagony chairs','living room',0)
h[0, -1] = Room(0,0,0,(-1,-1),'hallway','hallway',0)
h[0, -2] = Transition('a',(3,2),'clearing','You open the door and walk out into the clearign to the south of the house',0)
h[1, 2] = Wall()
h[1, 1] = Room(0,(1,0),0,0,'You are on a balcony with a path down to the east.','balcony',0)
h[1, 0] = Room((1,1),0,0,0,'You are in a dinng room, a large oval table sits in the center','dining room',0)
h[1, -1] = Room(0,0,0,0,'you are in the kitchen, cabinets line the walls','Kitchen',0)
h[1, -2] = Wall()
h[2, 1] = Transition('a',(4,3),'clearing','You step off the deck into the clearing around the house ',0)
h[2, 0] = Wall()
h[2, -1] = Wall()
