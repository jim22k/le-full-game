from .space import regions, Space, Transition, Fence, Cell, Swamp


class BigTree(Space):
    def __init__(self, bean):
        super().__init__()
        self.bean = bean

    def walked_in(self, gs):
        if self.bean == 0:
            self.print(
                'you are under the branches of a large tree in the clearing, carved into the bark it reads "going into the witches swamp is a fools errand, only the old farmer knows the way through"'
            )
            gs.tree = 1
            self.bean = 1
        else:
            self.print('Large tree')


class Hut(Space):
    def __init__(self, bean):
        super().__init__()
        self.bean = bean

    def walked_in(self, gs):
        self.print('you walk into the witches hut')
        if gs.amulet == 1:
            self.print('"I have nothing else to give you, other than a tip, to exit the swamp quickly, let the mist take you out"')
            return
        else:
            if self.bean == 0:
                self.print('''you go to the witch and ask about the amulet
                "You want WHAT!
                No! Never! 
                Begone from my sight, I CURSE THEE!!!
                
                you wake up outside the mist swamp, you feel woozy and cannot tell wich way is wich, verything you do feeling backwards"''')
                gs.coord = (-1,2)
                gs.mist = 1
                gs.add = 's'
                self.bean = 1
                return
        
            else:
                self.print('''You're back!
                So persistent, well take the amulet and leave me be
                and fine I will un curse you
        #################################
        #    ___                        # 
        #   /   \   You got the Amulet  #
        #   \   /                       #
        #    \_/    with this you can   #
        #    /:\    resist flames       #
        #    \_/                        #
        #################################
                    ''')
                gs.mist = 0
                gs.amulet = 1
                return


class MistPath(Space):
    def walked_in(self, gs):
        self.print('you continue walking in the mist, where you are, where you were, no one knows')
    

class Fogged(Space):
    def walked_in(self, gs):
        gs.mist = 0
        gs.add = 's'
        gs.coord = (-1,2)
        self.print('''The mist closes in on you
        
        You open your eyes, you are back on the path that leads into the mist''')


#################
# Swamp Region
#################
regions['s'] = s = {}

s[-3, -2] = Fence()
s[-3, -1] = Fence()
s[-3, 0] = Transition('f',(1,0),'Field','you walk back into the farmers fields',0)
s[-3, 1] = Fence()
s[-3, 2] = Fence()

s[-2, -5] = Swamp()
s[-2, -4] = Swamp()
s[-2, -3] = Swamp()
s[-2, -2] = Cell('Swamp','a large vine brushes across your face',0)
s[-2, -1] = Cell('Swamp  (path to north)','a large frog croaks on a log, then hops away',0)
s[-2, 0] = Cell('Swamp path  (e/w)','the path leads on to the west, bugs buzz around your head',0)
s[-2, 1] = Cell('Swamp  (path to south)','you step into a deep cold puddle',0)
s[-2, 2] = Cell('Swamp','you slip on a patch of moss',0)
s[-2, 3] = Swamp()

s[-1, -6] = Swamp()
s[-1, -5] = Cell('Swamp path  (n/e)','the path goes to the north and east',0)
s[-1, -4] = Cell('Swamp path  (n/s)','you stumble on a tree root, the path continues around the clearing',0)
s[-1, -3] = Cell('Swamp path  (s/e)','the path continues to the south around a clearing',0)
s[-1, -2] = Cell('Swamp  (path to south/east)','large tree roots poke up through the ground',0)
s[-1, -1] = Cell('Swamp  (path to north/east)','you start to sink down in the mud',0)
s[-1, 0] = Cell('Swamp path  (e/w)','large vines hang off of trees, the path leads onwnards',0)
s[-1, 1] = Cell('Swamp path  (s)','the path dead ends to the north, rocks poke up through the water leading onwards',0)
s[-1, 2] = Cell('Swamp','the swamp starts to thin out, the mud dries out to dirt',0)
s[-1, 3] = Transition('mist',(-2,0),'misty swamp','Mist swirles all around. You cannot see a path going in any direction',0)

s[0, -6] = Swamp()
s[0, -5] = Cell('Swamp path  (e/w)','you are on the southern part of the loop',0)
s[0, -4] = BigTree(0)
s[0, -3] = Cell('Swamp path  (n/e/w)','the path splits to the east and west to form a loop around a large tree',0)
s[0, -2] = Cell('Swamp path  (n/s)','the path has a large loop up ahead around a large tree',0)
s[0, -1] = Cell('Swamp path  (n/s)','you have to jump over puddles to continue southwards',0)
s[0, 0] = Cell('Swamp path  (s/w)','the path turns to the south, large puddles lining the path',0)
s[0, 1] = Cell('Swamp  (path to south)','something moves in the murkey water',0)
s[0, 2] = Cell('Swamp','large lily pads float on murkey water',0)
s[0, 3] = Swamp()

s[1, -6] = Swamp()
s[1, -5] = Cell('Swamp path  (n/w)','The path goes west and north',0)
s[1, -4] = Cell('Swamp path  (n/s)','the path leads onwards, thick goo bubbles to the east',0)
s[1, -3] = Cell('Swamp path  (s/w)','the path turns, going to the west and the south',0)
s[1, -2] = Cell('Swamp  (path to south/west)','a cold breeze comes from the east',0)
s[1, -1] = Cell('Swamp  (path to west)','the swamp continues',0)
s[1, 0] = Cell('Swamp  (path to west)','a large tree root pokes up out of the ground',0)
s[1, 1] = Cell('Swamp','a frog croaks nearby',0)
s[1, 2] = Cell('Swamp','the dirt sinks under your feet',0)
s[1, 3] = Swamp()

s[2, -7] = Swamp()
s[2, -6] = Swamp()
s[2, -5] = Swamp()
s[2, -4] = Swamp()
s[2, -3] = Swamp()
s[2, -2] = Swamp()
s[2, -1] = Swamp()
s[2, 0] = Swamp()
s[2, 1] = Swamp()
s[2, 2] = Swamp()


#################
# Mist Region
#################
regions['mist'] = mist = {}

mist[-2, -1] = Transition('s',(-1,2),'misty swamp','As you walk, the mist dissapates, you are back on the path that led into the mist',0)
mist[-2, 0] = MistPath()
mist[-2, 1] = MistPath()
mist[-2, 2] = MistPath()
mist[-2, 3] = MistPath()
mist[-1, 3] = MistPath()
mist[0, 3] = MistPath()
mist[0, 2] = MistPath()
mist[1, 2] = MistPath()
mist[1, 1] = MistPath()
mist[1, 0] = MistPath()
mist[2, 0] = MistPath()

mist[-3, 0] = Fogged()
mist[-3, 1] = Fogged()
mist[-3, 2] = Fogged()
mist[-3, 3] = Fogged()
mist[-2, 4] = Fogged()
mist[-1, 0] = Fogged()
mist[-1, 1] = Fogged()
mist[-1, 2] = Fogged()
mist[-1, 4] = Fogged()
mist[0, 0] = Fogged()
mist[0, 1] = Fogged()
mist[0, 4] = Fogged()
mist[1, 3] = Fogged()
mist[2, -1] = Fogged()
mist[2, 1] = Fogged()
mist[2, 2] = Fogged()

mist[3, 0] = Cell('Clearing','you walk into a clearing, a sign in the ground read "witches hut, STAY OUT!"',0)
mist[3, 1] = Cell('Clearing','here bones lay on top of wooden spikes stuck into the ground',0)
mist[3, -1] = Cell('Clearing','a large cauldron lets off puffs of smoke',0)
mist[3, 2] = Swamp()
mist[3, -2] = Swamp()
mist[4, 0] = Hut(0)
mist[4, 1] = Swamp()
mist[4, -1] = Swamp()
mist[5, 0] = Swamp()
mist[1, -1] = Fogged()
