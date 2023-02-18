import js
from Maps import print_map
from areas.space import regions
from areas import area1, area2, attic, castle, cave, field, house, orchard, swamp, volcano


class GameState:
    def __init__(self):
        self.coord = (0, 0)
        self.past_coords = self.coord
        self.player_fire = 0
        self.player_chop = 0
        self.has_wood = 0
        self.sword = 0
        self.magic = 0
        self.amulet = 0
        self.fairy = 0
        self.troll_life = 1
        self.pix = 0
        self.ggs = 0
        self.add = 'a'
        self.mist = 0
        self.button = 0
        self.tree = 0
        self.past_add = self.add
    
    def take_step(self, direction):
        self.past_coords = self.coord
        direction = direction.lower()[0]
        step = -1 if self.mist else +1
        x, y = self.coord
        if direction == 'n':
            y += step
        elif direction == 's':
            y -= step
        elif direction == 'e':
            x += step
        elif direction == 'w':
            x -= step
        self.coord = (x, y)

    def move(self, direction):
        if self.ggs == 2:
            return
        if self.ggs == 1:
            write_output('ggs mate\n\ngame over')
            # Disable buttons
            js.document.getElementById('up-button').setAttribute('disabled', True)
            js.document.getElementById('down-button').setAttribute('disabled', True)
            js.document.getElementById('right-button').setAttribute('disabled', True)
            js.document.getElementById('left-button').setAttribute('disabled', True)
            # Enable restart
            js.document.getElementById('restart-button').removeAttribute('disabled')

            self.ggs = 2
            return
        
        self.take_step(direction)
        space = regions[self.add][self.coord]
        space.walked_in(gs)
        write_output(space.flush())



# Game Object
gs = GameState()
outputs = js.document.getElementById("text")


def write_output(s):
    new_text = js.document.createElement('div')
    new_text.innerHTML = s
    outputs.insertBefore(new_text, outputs.firstChild)


# Button callbacks
def up():
    gs.move('n')
    print_map(gs)

def down():
    gs.move('s')
    print_map(gs)

def right():
    gs.move('e')
    print_map(gs)

def left():
    gs.move('w')
    print_map(gs)

def credits():
    write_output('''*deep inahle
    ya the whole game was made by me (Nathan Kitchen) lol
    so storyboard, creative design, artwork, all that jazz is me
    shoutout to my dad for helping with a project a while ago that I yoinked a bunch of code from
    also shoutout to Zork, Zelda, and Rakuen as inspiration
    ''')

def restart():
    global gs

    gs = GameState()
    outputs.innerHTML = ""
    # Disable restart button
    js.document.getElementById('restart-button').setAttribute('disabled', True)
    # Enable movement buttons
    js.document.getElementById('up-button').removeAttribute('disabled')
    js.document.getElementById('down-button').removeAttribute('disabled')
    js.document.getElementById('right-button').removeAttribute('disabled')
    js.document.getElementById('left-button').removeAttribute('disabled')
    
    # Initial text for player
    write_output("""Now let us begin:
  You are sitting in a forest. Larges trees hang all aroud. A dirt path runs north-south. Birds chirp in the distance.
  You stand up.""")
    print_map(gs)


restart()
