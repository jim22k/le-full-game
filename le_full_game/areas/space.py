import random

# Holds named grids of spaces
regions = {}

class Space:
    def __init__(self):
        self._output = []

    def walked_in(self, gs):
        raise NotImplementedError()
    
    def print(self, text):
        self._output.append(text)
    
    def flush(self):
        text = '\n'.join(self._output)
        self._output.clear()
        return text

###################################
# Common Spaces used in the games
###################################
class CaveWall(Space):
    def __init__(self, bean):
        super().__init__()
        self.bean = bean

    def walked_in(self, gs):
        if gs.pix == 0:
            self.print('There is a wall in the way')
            gs.coord = gs.past_coords
        else:
            if self.bean == 0:
                self.print('you break through the stone')
                self.bean = 1
            else:
                self.print('you walk through the new tunnel')


class Cell(Space):
    def __init__(self, name, text, bean):
        super().__init__()
        self.name = name
        self.text = text
        self.bean = bean

    def walked_in(self, gs):
        if self.bean == 0:
            self.print(self.text)
            self.bean = 1
        else:
            self.print(self.name)


class Chasm(Space):
    def walked_in(self, gs):
        self.print('the chasm blocks your path')
        gs.coord = gs.past_coords


class Darkness(Space):
    def __init__(self, text, kill, bean):
        super().__init__()
        self.text = text
        self.kill = kill
        self.bean = bean

    def walked_in(self, gs):
        if gs.player_fire != 1:
            if self.kill == 1:
                self.print('Something jumps out of the dark and eats you, ggs mate')
                gs.ggs = 1
            else:
                self.print('the forest is too dark to see')
        elif gs.player_fire == 1:
            if self.bean == 0:
                self.print(self.text)
                self.bean = 1
            else:
                self.print('Dark forest')


class Fence(Space):
    def walked_in(self, gs):
        self.print('Fence in the way')
        gs.coord = gs.past_coords


class Field(Space):
    def walked_in(self, gs):
        bored = random.randint(1,3)
        if bored == 1:
            self.print('More fields')
        elif bored == 2:
            self.print('the farmland continues')
        elif bored == 3:
            self.print('rows of crops are planted in neat lines')


class Forest(Space):
    def __init__(self, path):
        super().__init__()
        self.path = path

    def walked_in(self, gs):
        if self.path != '':
            pathadd = '  ' + '(' + self.path + ')'
        else: 
            pathadd = ''
        bored = random.randint(1,5)
        if bored == 1:
            self.print('The forest continues' + pathadd)
        elif bored == 2:
            self.print('Birds chrip all around' + pathadd)
        elif bored == 3:
            self.print('The forest buzzes with life' + pathadd)
        elif bored == 4:
            self.print('More forest' + pathadd)
        else:
            self.print('The forest continues onwards' + pathadd)


class River(Space):
    def walked_in(self, gs):
        self.print('the river blocks your path')
        gs.coord = gs.past_coords


class Slope(Space):
    def walked_in(self, gs):
        self.print('you cannot climb up the cliff here')
        gs.coord = gs.past_coords


class Swamp(Space):
    def walked_in(self, gs):
        self.print('the swamp it too deep and thick to get through')
        gs.coord = gs.past_coords


class Thick(Space):
    def __init__(self, text, bean):
        super().__init__()
        self.text = text
        self.bean = bean
    
    def walked_in(self, gs):
        if gs.player_chop != 1:
            self.print('the forest is to thick to go that way - an axe could cut through it though')
            gs.coord = gs.past_coords
        elif gs.player_chop == 1:
            if self.bean == 1:
                self.print('Thick forest')
            else:
                self.print(self.text)
                self.bean = 1


class Transition(Space):
    def __init__(self, nad, ncords, name, text, bean):
        super().__init__()
        self.nad = nad
        self.ncords = ncords
        self.name = name
        self.text = text
        self.bean = bean

    def walked_in(self, gs):
        gs.add = self.nad
        gs.coord = self.ncords
        if self.bean == 0:
            self.print(self.text)
            self.bean = 1
        else:
            self.print(self.name)

class Wall(Space):
    def walked_in(self, gs):
        self.print('There is a wall in the way')
        gs.coord = gs.past_coords


class Bridge(Space):
    def __init__(self, bean):
        super().__init__()
        self.bean = bean

    def walked_in(self, gs):
        if gs.has_wood == 0:
            self.print('the bridge is out')
            gs.coord = gs.past_coords
        else:
            if self.bean == 0:
                self.print('you lay the wood down and can now cross the chasm')
                self.bean = 1
            else:
                self.print('Chasm bridge')


class House(Space):
    def walked_in(self, gs):
        if gs.past_coords == (2, 3):
            self.print('there is no door here')
            gs.coord = gs.past_coords
        elif gs.past_coords == (3, 2):
            gs.coord = (0, -1)
            self.print('You are in a hallway with a door to the north and east')
            gs.add = 'h'
        elif gs.past_coords == (3, 4):
            self.print('no door here')
            gs.coord = gs.past_coords
        elif gs.past_coords == (4, 3):
            gs.coord = (1, 1)
            self.print('You are on a balcony with a path down to the east.')
            gs.add = 'h'
