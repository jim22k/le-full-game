from .space import regions, Space, Wall, Transition
from .item import Item


class Attic(Space):
    def __init__(self, text, bean):
        super().__init__()
        self.text = text
        self.bean = bean

    def walked_in(self, gs):
        if gs.player_fire != 1:
            self.print('It is too dark up here to see')
        elif gs.player_fire == 1:
            if self.bean == 0:
                self.print(self.text)
                self.bean = 1
            else:
                self.print('attic')


regions["attic"] = attic = {}

attic[0, 2] = Transition('h',(-1,1),'Down stairs','You walk down the attic stairs',0)
attic[0, 1] = Attic('You are in a large dusty attic',0)
attic[0, 0] = Attic('Dead bugs lay on the floor',0)
attic[1, 2] = Attic('Large boxes are piled up',0)
attic[1, 1] = Attic('the floorboards are well worn here',0)
attic[1, 0] = Attic('the floor boards creak as you walk over them',0)
attic[2, 2] = Attic('A rat scurries along the dusty floor',0)
attic[2, 1] = Attic('A large work station has many tools laying ontop on it',0)
attic[2, 0] = Item('Attic corner','''A bundle of wood is laying in the corner, you pick it up                 
##########################################       
#  |__|  /--/                            #
#  |- | / -/   You got the wood planks   #
#  | -|/- /                              #
#  | -| -/     with this you can lay     #   
#  |- |-/      them down to cross gaps   #
#  |--|/                                 #
##########################################
                 ''',0,0,0,0,0,1,1,0,0,0)

attic[3, 0] = Wall()
attic[3, 1] = Wall()
attic[3, 2] = Wall()
attic[0, 3] = Wall()
attic[1, 3] = Wall()
attic[2, 3] = Wall()
attic[-1, 0] = Wall()
attic[-1, 1] = Wall()
attic[-1, 2] = Wall()
attic[0, -1] = Wall()
attic[1, -1] = Wall()
attic[2, -1] = Wall()




