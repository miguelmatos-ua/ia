# Daniel Coelho de Oliveira - 96800
# Pedro Candoso - 86140
# Miguel Matos - 89124

import math

def get_inputs(path):
    # Refactor: Recursive?
    inputs=[]
    for i in range(len(path)-1):
        xdiff=path[i+1][0]-path[i][0]
        ydiff=path[i+1][1]-path[i][1]
        d=(xdiff,ydiff)
        if d == (-1,0):
            inputs.append("a")
        if d == (1,0):
            inputs.append("d")
        if d == (0,-1):
            inputs.append("w")
        if d == (0,1):
            inputs.append("s")
    return inputs

def distance(p1, p2):
    # Hypotenuse distance
    x1, y1 = p1
    x2, y2 = p2
    return math.hypot(x2 - x1, y2 - y1)

def manhattan_distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)
