import random
from .space import regions, Space, Transition, Cell, Wall
from .item import Item


class Prison(Space):
  total_steps = 0

  def walked_in(self, gs):
    Prison.total_steps += 1
    if Prison.total_steps > 30:
      self.print('you finalize realize you are going to die in this prison...')
      gs.ggs = 1
      return
    
    gottem = random.randint(1,5)
    if gottem == 1:
      self.print('you shuffle around in your Cell')
    elif gottem == 2:
      self.print('it is cold and dark, you can just make out the edges of the stones that keep you trapped')
    elif gottem == 3:
      self.print('you are going to be in here for a while')
    elif gottem == 4:
      self.print('a small drop of water plops to the ground')
    else:
      self.print('you shuffle around in your Cell')


class Keep(Space):
  def __init__(self, bean):
    super().__init__()
    self.bean = bean

  def walked_in(self, gs):
    if self.bean == 0:
      self.print('''You walk into the keep
      The kings points at you and asks "Are you the one who killed the troll?"
      The guard from the gate responds "Yes my lord"
      "Then send him to kill the dragon!"
      "Yes my lord"
      The guard walks over to you

      "To kill the dragon you will need a stronger sword, if you bring a fairy to the statue in the orchard to the north, a magical sword will appear"

      "You will also need an amulet to protect you from the dragon's breath, the witch who lives in the swamp to the east should be able to give you one"

      "Lastly, you need to find the entrance to the mountains in the cave up north, should be a pick around here somewhere."
      ''')
      self.bean = 1
      return
    else:
      if gs.fairy != 1:
        self.print('"You need to find a fairy, I think I saw one floating around a rock in a clearing in the forest"')
        self.print('')
      if gs.magic != 1:
        self.print('"You need to take the fairy to the statue in the orchard, a sword will then appear"')
        self.print('')
      if gs.amulet != 1:
        self.print('"You need to get an amulet from the witch who lives in the swamp to the east"')
        self.print('')
      if gs.pix != 1:
        self.print('You also need a pixkaxe to get through the cave and into the mountain, should be one around here')
        self.print('')
      if gs.pix == 1:
        self.print('"With that pickaxe you should be able to clear away rubble blocking the path to he mountains,the entrance is in the back of the cave where the troll lived"')
        self.print('')


class Jump(Space):
  def walked_in(self, gs):
    self.print('You cannot Jump off the castle Walls')
    gs.coord = gs.past_coords


########################
# Castle Region
########################
regions['c'] = c = {}

c[2, 0] = Cell('Castle yard','you are in the corner of the courtyard, large fancy floral formations line the edge of the Wall',0)
c[2, 1] = Cell('Castle yard','a cryptic message is scratched into the Wall, it reads "https://tinyurl.com/2s46xb2f" what could it mean?',0)
c[2, -1] = Cell('Castle yard','a large tree grows here, a sign in front of it reads "ye old king tree, planted by the 4 rd king of this castle"',0)
c[1, 0] = Keep(0)
c[1, 1] = Cell('Castle yard','you are to the north of the keep, large flags hang off of the keep Walls',0)
c[1, -1] = Cell('Castle yard','from here you can look up and see the guard protecting the tower, one of the guards looks down at you and yells "I LOST THE GAME!!"',0)
c[0, 2] = Transition('m',(-1,-5),'Castle gate','you walk out through the gate',0)
c[0, 1] = Cell('Castle yard','lush grass grows while the wind sweeps across the trees',0)
c[0, 0] = Cell('Castle yard','you are in the center of the courtyard, you are right next to the keep, doors on all four sides allow easy entry',0)
c[0, -1] = Cell('Castle Yard','a small fish pond hosts many colorful fish of many sizes',0)
c[-1, 0] = Cell('Castle yard','an empty hogdog stand sits in the courtyard, a sigh on it reads "Be back soon, need to restock on buns"',0)
c[-1, 1] = Cell('Castle yard','you walk past a guard, you nod to each other as you pass',0)
c[-1, -1] = Cell('Castle yard','the grass here is sparce, water from the Walls d r i p s down into the middle of a patch of dirt',0)
c[-2, 0] = Cell('Castle yard','a bench sits against the castle Wall, a plaque on the side reads "jimmothy timmons, troop 314, dedicated 01/10/0101"',0)
c[-2, 1] = Item('Castle yard','''a bright blue glowing pixelated picaxe floats above the ground, slowly rotating. As you get close to it, it flys into your hands
##################################################      
#       _________                                #
#     _|         |___                            #
#    |_              |      You got the pickaxe  #
#      |_______      |___                        #
#            _|          |                       #
#          _|    __      |  with this you can    #
#        _|    _|  |     |  break through stone  #
#      _|    _|    |     |                       #
#    _|    _|      |_   _|                       #
# __|    _|          |_|                         #
#|     _|                                        #
#|____|                                          #
##################################################    
                
                
                ''',0,0,0,0,0,0,0,1,0,0)

c[0, -2] = Wall()
c[1, 2] = Wall()
c[1, -2] = Wall()
c[2, 2] = Wall()
c[2, -2] = Wall()
c[3, 0] = Wall()
c[3, 1] = Wall()
c[3, -1] = Wall()
c[-1, 2] = Wall()
c[-1, -2] = Wall()
c[-2, -1] = Wall()
c[-2, 2] = Wall()
c[-3, 0] = Wall()
c[-3, 1] = Wall()


########################
# Prison Region
########################
regions['p'] = p = {}

p[-1, 0] = Wall()
p[-1, 1] = Wall()
p[0, -1] = Wall()
p[0, 0] = Prison()
p[0, 1] = Prison()
p[0, 2] = Wall()
p[1, -1] = Wall()
p[1, 0] = Prison()
p[1, 1] = Prison()
p[1, 2] = Wall()
p[2, 0] = Wall()
p[2, 1] = Wall()


########################
# Tower Region
########################
regions['t'] = t = {}

t[3, -2] = Cell('Castle Wall','the Wall splits going to the north and the east, the ladder down is to the west',0)
t[3, -1] = Cell('Castle Wall','You crawl to the north',0)
t[3, 0] = Cell('Castle Wall','now out of the gaurds view, you stand more upright',0)
t[3, 1] = Cell('Castle Wall','you try to keep the sounds of your feet to a minimum',0)
t[3, 2] = Cell('Castle Wall','the Wall turns to the west',0)
t[2, 2] = Cell('Castle Wall','looking out you can see the forest leading up to the castle',0)
t[1, 2] = Cell('Castle Wall','looking to the north/ east you cann see a small house in the fenced off fields',0)
t[0, 2] = Cell('Castle Wall','from here you can see right down the path leading into the forest',0)
t[-1, 2] = Cell('Castle Wall','looking south at the tower, the guards back is facing you',0)
t[-2, 2] = Cell('Castle Wall','the Wall continues',0)
t[-3, 2] = Cell('Castlle Wall','the Wall turns to the south',0)
t[-3, 1] = Cell('Castle Wall','nearing the door of the tower, you can see it is unlocked',0)
t[-3, 0] = Cell('Castle Wall','you are right next to the door into the tower',0)
t[-3, -1] = Cell('Castle tower','you open the door and walk into the tower, it is a small tight space with wepons hanging on the Walls',0)
t[-3, -2] = Cell('Castle tower','the tower is cold and damp',0)
t[-2, -1] = Item('Castle tower','''you walk to a weapon rack and take a sword
#######################################
#  / \                                #
#  | |     You picked up the sword    #
#  |.|                                #
#  |:|   With this you can stab stuff #
#`--8--'                              #
#   8                                 #
#   O                                 #
#######################################                   
                   ''',0,1,0,0,0,0,0,0,0,0)

t[-2, -2] = Cell('Castle tower','you are right next to the door out of the tower',0)
t[-1, -2] = Transition('p',(0,0),'guard','''as you open the door to leave the tower, the gaurds hops up and should "Hey! you should not be here!" He then hits you over the head



''',0)
t[0, -2] = Transition('p',(0,0),'guard','''as you shuffle on the floor, the guard calls out "Hey, you should not be here!", he then walks over and knocks you out



''',0)
t[1, -2] = Cell('Castle Wall','you huddle behind a barrel',0)
t[2, -2] = Cell('Castle Wall','you crawl into cover',0)
t[4, -2] = Transition('m',(2,-8),'Ladder','you climb down the ladder back to the ground',0)
t[4, -1] = Jump()
t[4, 0] = Jump()
t[4, 1] = Jump()
t[4, 2] = Jump()
t[-4, 0] = Jump()
t[-4, 1] = Jump()
t[-4, 2] = Jump()
t[-4, -1] = Wall()
t[-4, -2] = Wall()
t[2, 1] = Jump()
t[2, 3] = Jump()
t[2, -1] = Jump()
t[2, -3] = Jump()
t[1, 1] = Jump()
t[1, 3] = Jump()
t[1, -1] = Jump()
t[1, -3] = Jump()
t[0, 1] = Jump()
t[0, 3] = Jump()
t[0, -1] = Jump()
t[0, -3] = Jump()
t[-1, 1] = Jump()
t[-1, 3] = Jump()
t[-1, -1] = Wall()
t[-1, -3] = Jump()
t[-2, 1] = Jump()
t[-2, 3] = Jump()
t[-2, 0] = Wall()
t[-2, -3] = Jump()
t[-3, 3] = Jump()
t[-3, -3] = Jump()
t[3, 3] = Jump()
t[3, -3] = Jump()
