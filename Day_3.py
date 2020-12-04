from functools import reduce

"""part 1"""

def treecount(inp):
    inp = inp.split('\n')
    pos = 3
    trees = 0
    for x in inp[1:]:
        if pos >= len(x):
            pos -= len(x)
        if x[pos] == '#':
            trees += 1
        pos += 3
    return trees
        
"""part 2"""

def treecompare(inp):
    inp = inp.split('\n')
    positions = [[1,1],[3,1],[5,1],[7,1],[1,2]]
    treeresults = []
    for pos in positions:
        ph = 0
        trees = 0
        for i in range(1, len(inp)):
            if pos[1] == 1:
                ph += pos[0]
                if ph >= len(inp[i]):
                    ph -= len(inp[i])
                if inp[i][ph] == '#':
                    trees += 1
            else:
                if i % pos[1] == 0:
                    ph += pos[0]
                    if ph >= len(inp[i]):
                        ph -= len(inp[i])
                    if inp[i][ph] == '#':
                        trees += 1
        treeresults += [trees]
    return reduce((lambda x,y: x * y), treeresults)
