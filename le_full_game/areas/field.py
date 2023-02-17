from .space import regions, Space, Field, Fence, Transition, River, Forest, Cell, Chasm, Wall
from .item import Item


class FarmerHouse(Space):
    def walked_in(self, gs):
        self.print(
            'you are standing outside a small house, belonging to the farmer of these fields'
        )
        if gs.tree == 0:
            self.print('the farmer is not home')
        else:
            self.print('You ask the farmer how to get through the misty swamp')
            self.print('')
            self.print('''
"Going through there is a fools errand, but I guess I can tell you.

You want to go up four times, then right twice. After that go down, right, down, down.
Then it should be a straight shot to the witches hut to the east.

Be warned, she most likely will curse you, causing everything to look backwards if you do make it"''')


regions['f'] = f = {}

f[0, -5] = Field()
f[0, -4] = Field()
f[0, -3] = Field()
f[0, -2] = Field()
f[0, -1] = Field()
f[0, 0] = Field()
f[0, 1] = Field()
f[0, 2] = Field()

f[1, 2] = Field()
f[1, 1] = Field()
f[1, 0] = Field()
f[1, -1] = Field()
f[1, -2] = Field()
f[1, -3] = Field()
f[1, -4] = Field()
f[1, -5] = Field()

f[-1, -4] = Field()
f[-1, -5] = Field()
f[-2, -5] = Field()
f[-2, -4] = FarmerHouse()
f[-3, -4] = Fence()
f[-3, -5] = Fence()
f[-1, 1] = Fence()
f[-1, 2] = Fence()
f[-1, -1] = Fence()
f[-1, -2] = Fence()
f[-1, -3] = Fence()
f[-1, -6] = Fence()
f[-2, -3] = Fence()
f[-2, -6] = Fence()
f[-3, 4] = Fence()
f[-3, 5] = Fence()
f[0, 3] = Fence()
f[0, -6] = Fence()
f[1, 3] = Fence()
f[1, -6] = Fence()
f[2, 1] = Fence()
f[2, 2] = Fence()
f[2, -1] = Fence()
f[2, -2] = Fence()
f[2, -3] = Fence()
f[2, -4] = Fence()
f[2, -5] = Fence()
f[-1, 0] = Transition('m',(2,2),'Forest path','you walk out the gate and back into the forest',0)
f[2, 0] = Transition('s',(-2,0),'Swamp path','you walk into a swamp, large willow trees hang low and murky water swirles in small puddles',0)
