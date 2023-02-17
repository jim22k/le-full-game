from .space import regions, Space, Cell, Transition, Slope, Fence

class SlopeBack(Space):
  def walked_in(self, gs):
    self.print('you slide down the cliff')
    gs.coord = (3,-5)
    gs.add = 'vd'

class SlopeRight(Space):
  def walked_in(self, gs):
    self.print('you slide down the cliff')
    gs.coord = (5,0)
    gs.add = 'vd'

class SlopeLeft(Space):
  def walked_in(self, gs):
    self.print('you slide down the cliff, down to the deepest part of the valley')
    gs.coord = (0,0)
    gs.add = 'vd'

class VolcBridge(Space):
  def __init__(self, bean):
    super().__init__()
    self.bean = bean

  def walked_in(self, gs):
    if gs.button == 0:
      if self.bean == 0:
        self.print('a bridge hangs down, making it impossible to continue up the path')
        self.bean = 1
      else:
        self.print('the bridge is out')
      gs.coord = gs.past_coords
      return
    elif gs.button == 1:
      self.print('you walk across the bridge')
      return

class VolcButton(Space):
  def __init__(self, bean):
    super().__init__()
    self.bean = bean

  def walked_in(self, gs):
    if self.bean == 0:
      self.print('''you walk over to a pedestal with a large button on it
      next to the button reads "Bridge closed for safety" 
      you press the button. The bridge to the north lifts up''')
      self.bean = 1
      gs.button = 1
    else:
      self.print('volcano bridge button')

class Dragon(Space):
    def walked_in(self, gs):
        self.print('''You walk into the open area
    A large dragon swoops in from below the ridge and lands in front of you
             __                  __               
            ( _)                ( _)              
           / / \\\              / /\_\_            
          / /   \\\            / / | \ \           
         / /     \\\          / /  |\ \ \          
        /  /   ,  \ ,       / /   /|  \ \         
       /  /    |\_ /|      / /   / \   \_\        
      /  /  |\/ _ '_| \   / /   /   \    \\\       
     |  /   |/  0 \\0\    / |    |    \    \\\      
     |    |\|      \_\_ /  /    |     \    \\\     
     |  | |/    \.\ o\o)  /      \     |    \\\    
     \    |     /\\\`v-v  /        |    |     \\\   
      | \/    /_| \\\_|  /         |    | \    \\\  
      | |    /__/_ `-` /   _____  |    |  \    \\\ 
      \|    [__]  \_/  |_________  \   |   \    ()
       /    [___] (    \         \  |\ |   |   //
      |    [___]                  |\| \|   /  |/
     /|    [____]                  \  |/\ / / ||
    (  \   [____ /     ) _\      \  \    \| | ||
     \  \  [_____|    / /     __/    \   / / //
     |   \ [_____/   / /        \    |   \/ //
     |   /  '----|   /=\____   _/    |   / //
  __ /  /        |  /   ___/  _/\    \  | ||
 (/-(/-\)       /   \  (/\/\)/  |    /  | /
               (/\/\)           /   /   //
                      _________/   /    /
                     \____________/    (
    ''')
        if gs.amulet != 1:
            self.print('the dragon breaths fire all over, killing you')
        else:
            self.print(
                'the dragon breaths fire all over you, but the amulet keeps you safe'
            )
        if gs.magic != 1:
            self.print('''
      you charge the dragon, swinging your sword
      it bounces off the dragon, breaking in half

      the dragon swipes its claws at you, killing you
      ''')
        else:
            self.print(
                '''you charge the dragon and stab it in the heart with your sword, killing it
      good job u won lol
      you can type "credits" to see the credits if you want''')
        gs.ggs = 1


######################
# Lower Volcano Region
######################
regions['vd'] = vd = {}

vd[0, 0] = Cell('Volcano ravine','you are at the bottom of the ravine, sharp cliff edges leave most paths blocked',0)
vd[1, 0] = Cell('Volcano ravine','you make your way through the ravine, slighty increasing your elevation',0)
vd[1, -1] = Cell('Volcano ravine','the path continues leading upwards',0)
vd[1, -2] = Cell('Volcano ravine','the path through the ravine, another path splits off to the east, leading downwards',0)
vd[1, -3] = Cell('Volcano ravine','the path leads up to the top of the ravine',0)

vd[5, 0] = Cell('Volcano ravine','you are at the bottom of the ravine',0)
vd[5, -1] = Cell('Volcano ravine','the path leads up to ravine',0)
vd[5, -2] = Cell('Volcano ravine','the path turns to the west, it leads on underneath the path to the top of the mountain',0)
vd[4, -2] = Cell('Volcano ravine','ravine continues leading up',0)
vd[3, -2] = Cell('Volcano ravine','you are at the entrance to a tunnel underneath the escarpment',0)
vd[2, -2] = Cell('Volcano ravine','you are underneath the path to the top of the mountain, the bridge hands above you',0)
vd[1, -2] = Cell('Volcano ravine','the path connects to another path',0)

vd[1, -4] = Transition('v',(1,-4),'Volcano path','A sigh in the ground reads "now that you have climbed out, you might as well head back home, the view isnt really worth it" you climb up to the top of the ravine, you can now continue climbing to the top of the mountain',0)

vd[3, -5] = Cell('Volcano ravine','you are at the bottom of the ravine, a path leads up to the north',0)
vd[3, -4] = Cell('Volcano ravine','the path goes under the ridge up above',0)
vd[3, -3] = Cell('Volcano ravine','the path connects up with another path that leads east up ahead',0)

vd[4, -5] = Slope()
vd[3, -6] = Slope()
vd[2, -5] = Slope()
vd[-1, 0] = Slope()
vd[0, 1] = Slope()
vd[0, -1] = Slope()
vd[0, -2] = Slope()
vd[0, -3] = Slope()
vd[1, 1] = Slope()
vd[2, 0] = Slope()
vd[2, -1] = Slope()
vd[2, -3] = Slope()
vd[3, -1] = Slope()
vd[4, 0] = Slope()
vd[4, -1] = Slope()
vd[4, -3] = Slope()
vd[5, 1] = Slope()
vd[5, -3] = Slope()
vd[6, 0] = Slope()
vd[6, -1] = Slope()
vd[6, -2] = Slope()
vd[4, -4] = Slope()
vd[2, -4] = Slope()


######################
# Upper Volcano Region
######################
regions['v'] = v = {}

v[-1, -4] = Cell('Volcano path  (n/e/w)','the path splits to the north, to the viewing point, east to lead up the mountain, and west back into the caves',0)
v[-1, -3] = Cell('Volcano path  (n/s)','the path continues to the north, leading up to a viewing point',0)
v[-1, -2] = Cell('Volcano path  (n/s)','You climb up a flight of stairs',0)
v[-1, -1] = Cell('Viewpoint  (s)','you climb up to a view point that looks out over the mountain. A skinny path winds up to the very top, with a bridge starting the path, a path also leads to the west past the bridge',0)
v[0, -4] = Cell('Volcano path  (e/w)','the path leads on to the east',0)
v[1, -4] = Cell('Volcano path  (e/w)','the cliff side looks climbable to the north, it appears to split up ahead',0)
v[2, -4] = Cell('Volcano path (n/e/w)','the path splits, leading north and east',0)
v[3, -4] = Cell('Volcano path  (e/w)','small rocks tumble down the cliff as you shake the ground',0)
v[4, -4] = Cell('Volcano path  (n/w)','the path becomes harder to see',0)
v[4, -3] = VolcButton(0)

v[2, -3] = Cell('Volcano path  (n/s)','the path leads north, you are right next to the bridge',0)
v[2, -2] = VolcBridge(0)
v[2, -1] = Cell('Volcano path  (s/e)','the path up winds to the east',0)
v[3, -1] = Cell('Volcano path  (n/w)','the ridge turns back to the north, leading almost to the top of the mountain',0)
v[3, 0] = Cell('Volcano path  (n/s)','loose rocks roll down the cliff as you wak past them',0)
v[3, 1] = Cell('Volcano path  (n/s)','as you look behind you, you can see the network of valleys formed by erosion over many years',0)
v[3, 2] = Cell('Volcano path  (s/w)','the path turns to the west to make the trek to the top',0)
v[2, 2] = Cell('Volcano path  (e/w)','the cliff on either side of you grows steeper',0)
v[1, 2] = Cell('Volcano path  (e/w)','as you peer over the edge, you can see the lowest point of the valley',0)
v[0, 2] = Cell('Volcano path  (n/e)','the path makes one last turn to the north, a sign in the ground reads "Warning, proceeding will end with the loss of your life"',0)
v[0, 3] = Cell('Volcano path  (n/s)','the path flattens out upahead, ending abruptly',0)

v[0, 4] = Dragon()
v[-3, -4] = Transition('cave',(5,-2),'cave tunnel','you walk back into the cave tunnel',0)
v[-2, -4] = Cell('Volcano path (e/w)','the path starts to wind p to the top of the basin',0)
v[-2, 0] = Slope()
v[-1, 0] = Fence()
v[-2, -2] = Slope()
v[-2, -3] = Slope()
v[-2, -5] = Slope()
v[-2, -1] = Slope()
v[0, -2] = SlopeLeft()
v[0, -3] = SlopeLeft()

# Slopes
v[-1, 3] = SlopeLeft()
v[-1, 2] = SlopeLeft()
v[0, 1] = SlopeLeft()
v[0, -1] = SlopeLeft()
v[0, -2] = SlopeLeft()
v[0, -3] = SlopeLeft()
v[1, 1] = SlopeLeft()
v[2, 1] = SlopeLeft()
v[2, 0] = SlopeLeft()
v[1, -1] = SlopeLeft()
v[1, -2] = SlopeLeft()
v[1, -3] = SlopeLeft()

v[1, 3] = SlopeRight()
v[2, 3] = SlopeRight()
v[3, 3] = SlopeRight()
v[3, -2] = SlopeRight()
v[3, -3] = SlopeRight()
v[4, 2] = SlopeRight()
v[4, 1] = SlopeRight()
v[4, 0] = SlopeRight()
v[4, -1] = SlopeRight()
v[4, -2] = SlopeRight()
v[5, -3] = SlopeRight()
v[5, -4] = SlopeRight()

v[-1, -5] = SlopeBack()
v[0, -5] = SlopeBack()
v[1, -5] = SlopeBack()
v[2, -5] = SlopeBack()
v[3, -5] = SlopeBack()
v[4, -5] = SlopeBack()