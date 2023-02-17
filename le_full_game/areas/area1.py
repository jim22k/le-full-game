from .space import regions, Space, Cell, Transition, Chasm, River, Thick, Darkness, House, Bridge
from .item import Item

regions["a"] = a = {}

a[-5, 1] = Transition('orch',(2,0),'orchard','The forest turns into a bright glowing orchard with fruit trees in neat lines',0)

a[-4, 0] = Chasm()
a[-4, 1] = Darkness('Leaves swirl all around, a trail of them leading west grows more pronounced',0,0)
a[-4, 2] = River()

a[-3, -1] = Chasm()
a[-3, 0] = Darkness('Something runs to the east just outside of your vision',1,0)
a[-3, 1] = Darkness('a line of leaves runs east/west',1,0)
a[-3, 2] = Darkness('a river runs to the north and west',1,0)
a[-3, 3] = River()

a[-2, -2] = Chasm()
a[-2, -1] = Darkness('the fog is so dense you can just barley see the edge of the chasm it drops into',0,0)
a[-2, 0] = Darkness('The forest grows silent, and cold, your torchlight pierces through a dense swirling fog',0,0)
a[-2, 1] = Darkness('As the flickering torch illuminates the trees, you notic a faint trail of leaves leads to the west',0,0)
a[-2, 2] = Darkness('A low wooshing sound comes from the north',0,0)
a[-2, 3] = Darkness('the torchlight bounces off a fast moving river',0,0)
a[-2, 4] = River()

a[-1, -4] = Chasm()
a[-1, -3] = Chasm()
a[-1, -2] = Chasm()
a[-1, -1] = Cell('forest edge  (path to east)','the forest opens up out to a deep chasm',0)
a[-1, 0] = Cell('forest  (path to east)','the leaves of the trees begin to grow closer together',0)
a[-1, 1] = Cell('forest  (path to east)','The forest grows darker',0)
a[-1, 2] = Cell('forest  (path to east)','birds chip in the distance, the leaves get thicker and blot out more sun', 0)
a[-1, 3] = Cell('forest opening  (path to east)','A path leads out of the forest to the east',0) 
a[-1, 4] = Cell('forest','the forest leads up to a river bank',0)
a[-1, 5] = River()

a[0, -4] = Transition('m',(0,5),'Forest bridge','You cross the bridge, the path continues onward to the south',0)
a[0, -3] = Bridge(0)
a[0, -2] = Cell('forest edge  (n/s)','The path pops out of the forest, you are on a ridge over a deep chasm, with sheer Walls down to the east and west, the bridge to the south seems to be out.',0)
a[0, -1] = Cell('forest path  (n/s)','The path continues onward, getting slightly lighter with each step',0)
a[0, 0] = Cell('forest path (n/s)','The path runs north-south with trees all around',0)
a[0, 1] = Cell('forest path  (n/s)','The path continues to the north, a sign is in the ground at an odd angle with the words "Where is silksong" crudely carved into it',0)
a[0, 2] = Cell('forest path  (n/s)','Large leaves crunch underfoot, the sun shines brightly down through the trees',0)
a[0, 3] = Cell('forest path  (s/e)','The path turns to the east, you can make out something in the distance. the path streching south seems to go forever',0)
a[0, 4] = Cell('forest  (path to south)','Through the forest, a river rushes to the east and west. It is too deep to cross',0)
a[0, 5] = River()

a[1, -4] = Chasm()
a[1, -3] = Chasm()
a[1, -2] = Chasm()
a[1, -1] = Cell('forest  (path to west)','the forest looks out over a large chasm, to continue would not be a good idea',0)
a[1, 0] = Cell('forest  (path to west)', 'the forest seems to go on and on forever',0)
a[1, 1] = Cell('forest  (path to west)', 'large dark trees stretch out for what seems like forever',0)
a[1, 2] = Cell ('forest  (path to west)','off the path, a very large fallen log lays on the ground',0)
a[1, 3] = Cell('forest path  (e/w)','the forest thins out to the east, you can see a building in a clearing outside of the forest',0)
a[1, 4] = Cell('forest  (path to south)','birds chirp loudly, a river rushes to the north, what a beautiful day it is',0)
a[1, 5] = Cell('forest/river bank','You are standing on the south side of a river, it is too deep to cross, to the west it gets louder',0)
a[1, 6] = River()

a[2, -2] = Chasm()
a[2, -1] = Thick('The forest tangle grows all the way to the bottom on a chasm to the south',0)
a[2, 0] = Thick('You chop your way through the deep foliage',0)
a[2, 1]= Thick('As you cut into the forest, you notice it has gone silent',0)
a[2, 2] = Cell('clearning  (house to north-east)', 'you are in a clearing that continues around a house to the north east.',0)
a[2, 3] =Cell('clearing  (house to east)','you are in a clearing, with a house to the east, the forest on very thick to the south, but thins to the west', 0)
a[2, 4] = Cell('clearing  (house to suoth-east)','the clearing continues around the house',0)
a[2, 5] = Cell('forest/river bank','the forest opens up to the bank of a river',0)
a[2, 6] = River()

a[3, -2] = Chasm()
a[3, -1] = Thick('A foul stench comes from the east',0)
a[3, 0] = Cell('forest clearing','The forest opens up into a clearing, a half eaten carcass is rotting on the groud to the south west',0)
a[3, 1] = Thick('As you clear your way through the forest, a foul stench blows up from the south',0)
a[3, 2] = Cell('clearing  (house to the north)','you are in a clearing to the south of a house, A path leads up to the door of the house. The forest to the south is quite dense',0)
a[3, 3] = House()
a[3, 4] = Cell('clearing  (house to the south)','You are on the north side of the house, a balcony looks out from the house at you',0)
a[3, 5] = Cell('forest/ river bank','the forest leads up to the edge of a river',0)
a[3, 6] = River()

a[4, -1] = Transition('cave',(0,0),'Cave entrance','you walk into the entrance to a large cave, littering the floor are bones of animals.',0)
a[4, 0] = Thick('The forest leads up to the edge of the chasm, thick brush prevents you from seeing the edge',0)
a[4, 1] = Thick('The forest smells of blood',0)
a[4, 2] = Cell('clearing  (house to north-west)','You are in a clearing to the south- east of a house, the forest grows very deep to the south',0)
a[4, 3] = Cell('clearing  (house to west)','You are in a clearing to the east of a house',0)
a[4, 4] = Cell('clearing  (house to south-west)','you are on the north-eastern tip of the clearing around the house',0)
a[4, 5] = Cell('forest','the forest leads up to a river bank',0)
a[4, 6] = River()

a[5, 0] = Chasm()
a[5, 1] = Item('forest','''an axe is in a log, you pick it up

###################################
#   _,-,                          #
#  T_  |  You got the Wood Axe    #
#  ||`-'                          #
#  ||     with this you can cut   #
#  ||     through dense foliage   #
#  ~~                             #
###################################            ''',0,0,0,0,0,0,0,0,1,0)

a[5, 2] = Cell('forest','many fallen logs litter the forest floor',0)
a[5, 3] = Cell('forest','A tree has been carved with the letters "D E F G E C D"',0)
a[5, 4] = Cell('forest','a song birds flys across the path, landing in a different tree',0)
a[5, 5] = Cell('forest','ive read the word forest so many times it has lost its meaning',0)
a[5, 6] = River()

a[6, 1] = River()
a[6, 2] = River()
a[6, 3] = River()
a[6, 4] = River()
a[6, 5] = River()
