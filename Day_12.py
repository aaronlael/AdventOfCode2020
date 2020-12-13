# part 1

def manhattan(inp):
    dirclockwise = ['N','E','S','W']
    currentdirection = 'E'
    distance = { x:0 for x in dirclockwise }
    out = {}
    for v in inp:
        currentdirection, out = dirdist(v, currentdirection, dirclockwise)
        distance[list(out.keys())[0]] += out[list(out.keys())[0]]
        # print(distance, v, out, currentdirection)


    return abs(distance['E'] - distance['W']) + abs(distance['N'] - distance['S'])

def dirdist(val, currentdirection, dirclockwise):
    d = val[0]
    u = int(val[1:])
    if d in ('R', 'L'):
        u = int(u/90)
        for i in range(len(dirclockwise)):
            if dirclockwise[i] == currentdirection:
                if d == 'R': 
                    if (i + u) >= len(dirclockwise):
                        currentdirection = dirclockwise[(i + u) - len(dirclockwise)]
                    else:
                        currentdirection = dirclockwise[i+u]
                else:
                    currentdirection = dirclockwise[i-u]
                return currentdirection, { 'N':0 }

    else:
        if d == 'F':
            return currentdirection, { currentdirection: u}
        elif d in dirclockwise:
            return currentdirection, { d : u }
        else:
            return currentdirection, {'N',0}
        

# part 2


def hatmannin(inp):
    waypoint = { 'N': 1, 'E':10, 'S': 0, 'W': 0 }
    ship = { 'N': 0, 'E':0, 'S': 0, 'W': 0 }
    for val in inp:
        if val[0] in ('N','E','S','W'):
            waypoint = waycalc(waypoint, val)
        elif val[0] in ('L', 'R'):
            waypoint = rotate(waypoint, val)
        else:
            ship = shipmove(ship, waypoint, val)
    return (ship['N'] + ship['S']) + (ship['E'] + ship['W'])

def waycalc(waypoint, val):
    oppose = { 'N': 'S', 'E': 'W', 'S' : 'N', 'W': 'E'}
    if waypoint[oppose[val[0]]] == 0:
        waypoint[val[0]] += int(val[1:])
    elif waypoint[oppose[val[0]]] - int(val[1:]) < 0:
        waypoint[val[0]] = int(val[1:]) - waypoint[oppose[val[0]]]
        waypoint[oppose[val[0]]] = 0
    else:
        waypoint[oppose[val[0]]] = waypoint[oppose[val[0]]] - int(val[1:])    
    return waypoint

def shipmove(ship, waypoint, val):
    oppose = { 'N': 'S', 'E': 'W', 'S' : 'N', 'W': 'E'}
    modifier = int(val[1:])
    way = { 'N': 0, 'E':0, 'S': 0, 'W': 0 }
    for k in way.keys():
        way[k] = waypoint[k] * modifier
        if way[k] > 0:
            if ship[k] > 0:
                ship[k] = ship[k] + way[k]
            elif ship[oppose[k]] > 0:
                if ship[oppose[k]] - way[k] >= 0:
                    ship[oppose[k]] = ship[oppose[k]] - way[k]
                else:
                    ship[k] = way[k] - ship[oppose[k]]
                    ship[oppose[k]] = 0
            else:
                ship[k] = way[k]
    return ship
    
def rotate(waypoint, val):
    wayout = { 'N': 0, 'E':0, 'S': 0, 'W': 0 }
    n = int(int(val[1:])/90)
    if val[0] == 'R':
        for i in range(n):
            wayout['N'], wayout['E'], wayout['S'], wayout['W'] = waypoint['W'],waypoint['N'],waypoint['E'],waypoint['S']
            waypoint = wayout
    elif val[0] == 'L':
        for i in range(n):
            wayout['N'], wayout['E'], wayout['S'], wayout['W'] = waypoint['E'],waypoint['S'],waypoint['W'],waypoint['N']
            waypoint = wayout
    
    return waypoint

