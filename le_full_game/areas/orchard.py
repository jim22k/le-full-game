from .space import regions, Space, Cell, Transition


class Cliff(Space):
  def walked_in(self, gs):
    self.print('cliff in the way')
    gs.coord = gs.past_coords


class Statue(Space):
    def __init__(self, bean, got):
        super().__init__()
        self.bean = bean
        self.got = got

    def walked_in(self, gs):
        if self.bean == 0:
            self.print(
                'a tall statue of a knight stands on a pedestal, parts of the stone are cracked, and moss grows over the surface'
            )
            self.bean = 1
        if gs.fairy == 1 and gs.sword == 1:
            if self.got == 0:
                self.print(' ')
                self.print(
                    '''you let the fairy fly out of your hands, it swirles around the top of the statue.
a shimmer of light appears in front of the statue, and your sword begins glowing
###############################################
#       /| ________________                   #
# O|===|* >________________>                  #
#       \|                                    #
#         You got the magic sword             #
#  with this, not even dragons stand a chance #
#                                             #
###############################################
              ''')
                gs.magic = 1
                self.got = 1

        self.print('the statue sits lifelessly')


# Orchard
regions['orch'] = orch = {}

orch[2, 0] = Cell('Orchard','Orchard',0)
orch[1, 0] = Cell('Orchard','A main path through the orchard leads to the east',0)
orch[0, 0] = Cell('Orchard','The path continues, sharp cliff walls on the outside of the orchard angle inwards',0)
orch[-1, 0] = Cell('Orchard','The cliff walls pinch closer leading up to a tall statue',0)
orch[-2, 0] = Statue(0,0)
orch[2, 1] = Cell('Orchard','here is an apple tree, with large juicy apples growing on it',0)
orch[2, -1] = Cell('Orchard','A sign in placed in front of a tree reading PEAR TREE, on the tree apples grow',0)
orch[1, 1] = Cell('Orchard','hundreds or cherries hang from a tree',0)
orch[1, -1] = Cell('Orchard','A freshly grafted branch bears fruit on the left side of a tree',0)
orch[0, 1] = Cell('Orchard','Behind a fruit tree, tall cliff walls hoot up to the sky',0)
orch[0, -1] = Cell('Orchard','A banana tree hangs low to the ground, drooping under the weight on a thousand bananas',0)
orch[3, 0] = Transition('a',(-4,1),'Forest','You walk out of the orchard back into the forest',0)
orch[3, 1] = Cliff()
orch[2, 2] = Cliff()
orch[1, 2] = Cliff()
orch[0, 2] = Cliff()
orch[-1, 1] = Cliff()
orch[-2, 1] = Cliff()
orch[-3, 0] = Cliff()
orch[-2, -1] = Cliff()
orch[-1, -1] = Cliff()
orch[0, -2] = Cliff()
orch[1, -2] = Cliff()
orch[2, -2] = Cliff()
orch[3, -1] = Cliff()
