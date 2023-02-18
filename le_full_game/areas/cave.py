from .space import regions, Space, Cell, Transition, Wall, CaveWall

class Troll(Space):
  '''im the grumpy old troll who lives under the bridge'''
  def walked_in(self, gs):
    if gs.troll_life == 1:
      if gs.sword != 1 and gs.magic != 1:
        self.print('the troll reaches out, you try to dodge, but it catches and eats you.')
        gs.ggs = 1
      else:
        self.print('the troll tries to run away, but you chop its head off before it can leave the cave.')
        gs.troll_life = 0
    else:
      self.print('the trolls dead body lays on the ground of the cave')


# cave
regions['cave'] = cave = {}

cave[-1, 0] = Transition('a',(3,-1),'Thick forest','you walk out of the cave to the west',0)
cave[-1, -1] = Wall()
cave[0, 1] = Transition('a',(4,0),'Thick forest','you walk out of the cave to the north',0)
cave[0, 0] = Cell('Cave entrance','you are standing in the exit of the cave',0)
cave[0, -1] = Cell('Cave','the farther into the cave you go, the worse it smells',0)
cave[0, -2] = Wall()
cave[1, 1] = Wall()
cave[1, 0] = Cell('Cave','as you walk deeper into the cave, it grows much darker',0)
cave[1, -1] = Cell('Cave','the cave gets tighter, only leading to the west',0)
cave[1, -2] = Wall()
cave[2, 0] = Wall()
cave[2, -1] = Cell('Cave','the cave opens back up, the stench of the troll is greater still. A growl to the south makes you jump',0)
cave[2, -2] = Troll()
cave[2, -3] = Wall()
cave[3, -1] = Wall()
cave[3, -2] = CaveWall(0)
cave[3, -3] = Wall()
cave[4, -1] = Wall()
cave[4, -2] = CaveWall(0)
cave[4, -3] = Wall()
cave[5, -1] = Wall()
cave[5, -2] = CaveWall(0)
cave[5, -3] = Wall()
cave[6, -2] = Transition('v',(-2,-4),'','You break out of the rock and into the basin of a volcano',0)
