from .space import regions, Space, Field, Fence, Transition, River, Forest, Cell, Chasm, Wall, FarmerHouse
from .item import Item

class Gate(Space):
  def __init__(self, bean):
    super().__init__()
    self.bean = bean

  def walked_in(self, gs):
    self.print(''' you talk to the guard at the gate
    "Until the troll to the north is taken care of, the castle is off limits to visitors"
    ''')
    if gs.troll_life == 1:
      self.print('"Sorry, but we cannot allow you to enter the castle untill the troll to the north is taken care of"')
      gs.coord = gs.past_coords
    else:
      if self.bean == 0:
        self.print('"You killed the troll!?! well I guess I have no choice to let you in"')
        self.bean = 1
      else:
        self.print('you walk though the gate, nodding the guard as you pass by')


regions['m'] = m = {}

m[-4, -5] = River()
m[-4, -4] = River()
m[-4, -3] = River()
m[-4, -2] = River()
m[-4, -1] = River()
m[-4, 0] = River()
m[-4, 1] = River()
m[-4, 2] = River()
m[-4, 3] = River()
m[-4, 4] = River()

m[-3, -6] = Wall()
m[-3, -5] = Cell('Plains','You are right next to the castle wall and can see each stone',0)
m[-3, -4] = Cell('Plains','you can see a large tower on one corner of the castle',0)
m[-3, -3] = Forest('')
m[-3, -2] = Forest('')
m[-3, -1] = Forest('path to east')
m[-3, 0] = Forest('path to east')
m[-3, 1] = Forest('path to east')
m[-3, 2] = Forest('path to east')
m[-3, 3] = Forest('')
m[-3, 4] = Forest('')
m[-3, 5] = Chasm()

m[-2, -6] = Wall()
m[-2, -5] = Cell('Plains  path to east','You are right next to the castle walls',0)
m[-2, -4] = Cell('Plains  path to east','a grass hopper jumps in the tall grass',0)
m[-2, -3] = Forest('path to east')
m[-2, -2] = Forest('path to north and east')
m[-2, -1] = Cell('Forest path','the path turns to the east',0)
m[-2, 0] = Cell('Forest path','The path lead on',0)
m[-2, 1] = Cell('Forest path','A large puddle takes up the left half of the path',0)
m[-2, 2] = Cell('Forest path','The path turns to the south',0)
m[-2, 3] = Forest('path to south')
m[-2, 4] = Forest('')
m[-2, 5] = Chasm()

m[-1, -7] = Transition('c',(0,1),'Castle yard','you walk into the castle, a large courtyard is sourounded by tall Walls, the keep is to the south/east',0)
m[-1, -6] = Gate(0)
m[-1, -5] = Cell('Castle gates  (n/s)','You walk up to the gate. A gaurd stops you from entering. "We are in a state of lockdown, no one can enter the castle until the troll to the north is taken care of."',0)
m[-1, -4] = Cell('Plains path  (n/s)','the path leads up to the gates of the castle',0)
m[-1, -3] = Cell('Forest path  (n/s)','The path opens out of the forest and into plains surrounding a large castle',0)
m[-1, -2] = Cell('Forest path  (n/s)','the path leads on south',0)
m[-1, -1] = Cell('Forest path  (s/w)','the path turns back to the south, in the distance a large building dominates the landscape',0)
m[-1, 0] = Forest('path to west/south')
m[-1, 1] = Forest('path to north/west')
m[-1, 2] = Cell('Forest path  (e/w)','the path is much more defined here',0)
m[-1, 3] = Forest('path to south')
m[-1, 4] = Forest('')
m[-1, 5] = Chasm()

m[0, -6] = Wall()
m[0, -5] = Cell('Plains  (path to west)','You are right up against the castle walls',0)
m[0, -4] = Cell('Plains  (path to west)','as you leave the forest you can see a large castle in the distance',0)
m[0, -3] = Forest('')
m[0, -2] = Cell('Forest  (path to west)','more forets',0)
m[0, -1] = Forest('path to west')
m[0, 0] = Item('Fairy rock','''in a small clearing in the trees, a large rock sits. Upon closer insepction a small fairy floats around the top. You pick it up.
########################################
# .'.         .'.                      #
# |  \       /  |                      #
# '.  \  |  /  .'                      #
#   '. \\|// .'    You got the Fairy   #
#     '-- --'                          #
#     .'/|\'.                          #
#    '..'|'..'                         #
########################################
             ''',0,0,0,0,1,0,0,0,0,0)
m[0, 1] = Cell('Forest','The path ends and the trees grow thicker, and more at random',0)
m[0, 2] = Cell('Forest path  (n/w)','The path splits off to the east and west',0)
m[0, 3] = Cell('Forest path  (n/s)','tree roots poke up through the packed dirt',0)
m[0, 4] = Cell('Forest path  (n/s)','The path leads on to the south',0)
m[0, 5] = Cell('Forest path  (n/s)','the path quicky turns back into packed dirt',0)
m[0, 6] = Transition('a',(0,-3),'forest edge','You walk back along the make shift bridge',0)

m[1, -8] = Transition('t',(3,-2),'Castle wall corner','''You climb up the ladder and are now on the castle wall. You duck behind some barrels and take a look around.
To the west, the path along the walls lead up to a large tower, though a guard leans next to the entrace, yawning, it would be best to not be seen
                       
To the north the walls lead onwards, no guards in sight
                       
To the east the ladder hangs down, back to the ground
                       
To the south the wall drops into a sheer cliff''',0)
m[1, -7] = Wall()
m[1, -6] = Wall()
m[1, -5] = Cell('Plains','you are next to the castle wall',0)
m[1, -4] = Cell('Plains','The plains continue aroudn the castle',0)
m[1, -3] = Fence()
m[1, -2] = Fence()
m[1, -1] = Forest('')
m[1, 0] = Forest('')
m[1, 1] = Forest('path to north')
m[1, 2] = Cell('Forest path  (e/w)','The path goes to the east',0)
m[1, 3] = Forest('')
m[1, 4] = Forest('')
m[1, 5] = Chasm()

m[2, -9] = Fence()
m[2, -8] = Cell('Fence corner','Laying up against the wall is a small dark colored rope ladder that leads upwards',0)
m[2, -7] = Cell('Plains','You are in a narrow path between the castle wall and the farmers Fence',0)
m[2, -6] = Cell('Plains','you are on the east of the castle wall',0)
m[2, -5] = Cell('Plains','The plains continue',0)
m[2, -4] = Cell('Plains','You are next to a Fence',0)
m[2, -3] = Fence()
m[2, -2] = Fence()
m[2, -1] = Forest('')
m[2, 0] = Forest('')
m[2, 1] = Forest('path to north')
m[2, 2] = Cell('Forest path  (e/w)','The path leads to an open fance gate',0)
m[2, 3] = Forest('path to south')
m[2, 4] = Forest('')
m[2, 5] = Chasm()

m[3, -8] = Fence()
m[3, -7] = Fence()
m[3, -6] = Fence()
m[3, -5] = Fence()
m[3, -4] = Fence()
m[3, -1] = Fence()
m[3, 0] = Fence()
m[3, 1] = Fence()
m[3, 2] = Transition('f',(0,0),'Fields','You walk through the gate into fresh farmland',0)
m[3, 3] = Fence()
m[3, 4] = Fence()
