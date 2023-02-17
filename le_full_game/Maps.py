from pyscript import Element

#make all maps, add a fancy thingy to the coord + 7 thingy based on what add value, so you can have all maps shifted over the same ammout
map = {}
offset = {}

# map of area 1
#                          #  center          
map["a"] = [[0,0,0,0,0,0,0,4,4,4,4,4,4,4],
            [0,0,0,0,0,4,4,4,0,0,0,0,0,4],
            [0,0,0,0,4,4,0,0,0,1,1,1,0,4],
            [0,0,0,4,4,0,0,1,1,1,3,1,0,4],
            [0,4,4,4,0,0,0,1,0,1,1,1,0,4],
            [0,4,3,0,0,0,0,1,0,0,0,0,0,4],
            [0,4,4,4,0,0,0,1,0,0,0,0,4,4], # center
            [0,0,0,4,4,0,0,1,0,0,0,3,4,0],
            [0,0,0,0,4,4,4,1,4,4,4,4,4,0],
            [0,0,0,0,0,0,4,1,4,0,0,0,0,0],
            [0,0,0,0,0,0,4,3,4,0,0,0,0,0]]
offset["a"] = 6

#map of area 2
#                          #  center          
map["m"] = [[0,0,0,0,0,0,4,3,4,0,0,0,0,0],
            [0,0,0,4,4,4,4,1,4,4,4,0,0,0],
            [0,0,0,4,0,0,0,1,0,0,4,0,0,0],
            [0,0,0,4,0,0,0,1,0,0,4,0,0,0],
            [0,0,0,4,0,1,1,1,1,1,3,0,0,0],
            [0,0,0,4,0,1,0,0,0,0,4,0,0,0],
            [0,0,0,4,0,1,0,0,0,0,4,0,0,0], # center
            [0,0,0,4,0,1,1,0,0,0,4,0,0,0],
            [0,0,0,4,0,0,1,0,4,4,4,0,0,0],
            [0,0,0,4,0,0,1,0,4,4,4,0,0,0],
            [0,0,0,4,0,0,1,0,0,0,4,0,0,0],
            [0,0,0,4,0,0,1,0,0,0,4,0,0,0],
            [0,0,0,4,4,4,3,4,4,0,4,0,0,0],
            [0,0,0,0,0,0,0,0,4,0,4,0,0,0],
            [0,0,0,0,0,0,0,0,4,0,4,0,0,0],
            [0,0,0,0,0,0,0,0,4,4,4,0,0,0]]
offset["m"] = 6

#map of house
#                          #  center          
map["h"] = [[0,0,0,0,0,0,3,1,1,3,0,0,0,0],
            [0,0,0,0,0,0,1,1,1,0,0,0,0,0], # center
            [0,0,0,0,0,0,1,1,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,3,0,0,0,0,0,0]]
offset["h"] = 1

#map of attic
#                              #  center          
map["attic"] = [[0,0,0,0,0,0,0,3,1,1,0,0,0,0],
                [0,0,0,0,0,0,0,1,1,1,0,0,0,0],
                [0,0,0,0,0,0,0,1,1,1,0,0,0,0]] # center
offset["attic"] = 2

#map of cave
#                             #center          
map["cave"] = [[0,0,0,0,0,0,0,3,4,4,0,0,0,0],
               [0,0,0,0,0,0,3,0,0,4,4,0,0,0], # center
               [0,0,0,0,0,0,4,0,0,0,4,0,0,0],
               [0,0,0,0,0,0,4,4,4,0,4,0,0,0],
               [0,0,0,0,0,0,0,0,4,4,4,0,0,0]]
offset["cave"] = 1

#map of swamp
#                          #  center          
map["s"] = [[0,0,0,0,4,4,3,4,4,4,0,0,0,0],
            [0,0,0,0,4,0,1,0,0,4,0,0,0,0],
            [0,0,0,0,4,0,1,0,0,4,0,0,0,0],
            [0,0,0,0,3,1,1,1,0,4,0,0,0,0], # center
            [0,0,0,0,4,0,0,1,0,4,0,0,0,0],
            [0,0,0,0,4,0,0,1,0,4,0,0,0,0],
            [0,0,0,0,4,4,1,1,1,4,0,0,0,0],
            [0,0,0,0,0,4,1,0,1,4,0,0,0,0],
            [0,0,0,0,0,4,1,1,1,4,0,0,0,0],
            [0,0,0,0,0,4,4,4,4,4,0,0,0,0]]
offset["s"] = 3

#                          #  center          
map["f"] = [[0,0,0,0,0,0,4,4,4,4,0,0,0,0],
            [0,0,0,0,0,0,4,0,0,4,0,0,0,0],
            [0,0,0,0,0,0,4,0,0,4,0,0,0,0],
            [0,0,0,0,0,0,3,0,0,3,0,0,0,0], # center
            [0,0,0,0,0,0,4,0,0,4,0,0,0,0],
            [0,0,0,0,0,0,4,0,0,4,0,0,0,0],
            [0,0,0,0,4,4,4,0,0,4,0,0,0,0],
            [0,0,0,0,4,0,0,0,0,4,0,0,0,0],
            [0,0,0,0,4,0,0,0,0,4,0,0,0,0],
            [0,0,0,0,4,4,4,4,4,4,0,0,0,0]]
offset["f"] = 3


map["mist"] = [[4,4,4,4,4,4,4,4,4,4,4,4,4,4],
               [4,2,2,2,2,2,2,2,2,2,2,2,2,4],
               [4,2,2,2,2,2,2,2,2,2,2,2,2,4],
               [4,2,2,2,2,2,2,2,2,2,2,2,2,4],
               [4,2,2,2,2,2,2,2,2,2,2,2,2,4],
               [4,2,2,2,2,2,2,2,2,2,2,2,2,4],
               [4,2,2,2,2,2,2,2,2,2,2,2,2,4],
               [4,2,2,2,2,2,2,2,2,2,2,2,2,4], # center
               [4,2,2,2,2,2,2,2,2,2,2,2,2,4],
               [4,2,2,2,2,2,2,2,2,2,2,2,2,4],
               [4,2,2,2,2,2,2,2,2,2,2,2,2,4],
               [4,2,2,2,2,2,2,2,2,2,2,2,2,4],
               [4,2,2,2,2,2,2,2,2,2,2,2,2,4],
               [4,4,4,4,4,4,4,4,4,4,4,4,4,4]]
offset["mist"] = 7

                               #  
map["c"] = [[0,0,0,0,4,4,4,3,4,4,4,0,0,0],
            [0,0,0,0,4,0,0,0,0,0,4,0,0,0],
            [0,0,0,0,4,0,0,0,3,0,4,0,0,0], # center
            [0,0,0,0,4,4,0,0,0,0,4,0,0,0],
            [0,0,0,0,4,4,4,4,4,4,4,0,0,0]]
offset["c"] = 2

                           # le top ig  
map["t"] = [[0,0,0,4,4,4,4,4,4,4,4,4,0,0],
            [0,0,0,4,0,0,0,0,0,0,0,4,0,0],
            [0,0,0,4,0,4,4,4,4,4,0,4,0,0],
            [0,0,0,4,0,4,4,4,4,4,0,4,0,0], # center
            [0,0,0,4,0,0,4,4,4,4,0,4,0,0],
            [0,0,0,4,0,0,0,0,0,0,0,3,0,0],
            [0,0,0,4,4,4,4,4,4,4,4,4,0,0]]
offset["t"] = 3

                           #  
map["p"] = [[0,0,0,0,0,0,4,4,4,4,0,0,0,0],
            [0,0,0,0,0,0,4,0,0,4,0,0,0,0],
            [0,0,0,0,0,0,4,0,0,4,0,0,0,0], # center
            [0,0,0,0,0,0,4,4,4,4,0,0,0,0]]
offset["p"] = 2
 
                              # orch
map["orch"] = [[0,0,0,0,0,0,4,4,4,4,4,0,0,0],
               [0,0,0,0,4,4,4,0,0,0,4,0,0,0],
               [0,0,0,0,4,3,0,0,0,0,3,0,0,0], # center
               [0,0,0,0,4,4,4,0,0,0,4,0,0,0],
               [0,0,0,0,0,0,4,4,4,4,4,0,0,0]]
offset["orch"] = 2

                           #  
map["v"] = [[0,0,0,0,0,0,8,3,9,0,0,0,0,0],
            [0,0,0,0,0,0,8,1,9,9,9,9,0,0],
            [0,0,0,0,0,0,8,1,1,1,1,9,0,0],
            [0,0,0,0,0,0,8,8,8,8,1,9,0,0],
            [0,0,0,0,0,4,4,8,8,8,1,9,0,0], # center
            [0,0,0,0,0,4,1,8,8,1,1,9,0,0],
            [0,0,0,0,0,4,1,8,8,3,9,9,9,0],
            [0,0,0,0,0,4,1,8,8,1,9,1,9,0],
            [0,0,0,0,3,1,1,1,1,1,1,1,9,0],
            [0,0,0,0,0,8,8,8,8,8,8,8,8,0]]
offset["v"] = 4

                            # 
map["vd"] = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,4,4,4,4,0,4,4,4],
             [0,0,0,0,0,0,4,0,0,4,0,4,0,4], # center
             [0,0,0,0,0,0,4,4,0,4,4,4,0,4],
             [0,0,0,0,0,0,0,4,0,0,0,0,0,4],
             [0,0,0,0,0,0,0,4,0,4,0,4,4,4],
             [0,0,0,0,0,0,0,0,3,4,0,4,0,0],
             [0,0,0,0,0,0,0,0,0,4,0,4,0,0],
             [0,0,0,0,0,0,0,0,0,4,4,4,0,0]]
offset["vd"] = 7

#ight quick list of maps I need to make
# add a thingy liek hollow knight where you have to find the map percances


def print_map(gs):
    map_elem = Element("map")
    drawn = []

    #sets your coord to 2
    over = gs.coord[0] + 7
    y_offset = offset[gs.add]
    mappy = map[gs.add]
    attempt = mappy[y_offset - gs.coord[1]]
    spot = attempt[over]
    attempt[over] = 2

    #uses the correct map
    for row in mappy:
        mapadd = ""
        for cell in row:
            if cell == 1:
                mapadd = mapadd + "|_|"
            elif cell == 2:
                mapadd = mapadd + '|A|'
            elif cell == 3:
                mapadd = mapadd + "|#|"
            elif cell == 4:
                mapadd = mapadd + "|%|"
            elif cell == 5:
                mapadd = mapadd + "|A|"
            elif cell == 8:
                mapadd = mapadd + "///"
            elif cell == 9:
                mapadd = mapadd + "\\\\\\"
            else:
                # mapadd = mapadd + "   "
                mapadd = mapadd + "   "
        drawn.append(mapadd)
    attempt[over] = spot

    map_elem.write('\n'.join(drawn))