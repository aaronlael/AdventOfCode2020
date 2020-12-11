# part 1

def nearseats(seat, currentinp):
    lookaround = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    c = 0
    for lo in lookaround:
        try:
            if currentinp[seat[0]+lo[0]][seat[1]+lo[1]] == '#':
                c+=1
        except:
            continue
    return c
                              
def allseats(inp):
    nextseats = ['' for _ in range(len(inp))]
    for i in range(len(inp)):
        for j in range(len(inp[i])):
            if inp[i][j] != '.':
                c = nearseats((i,j),inp)
                if c == 0 and inp[i][j] == 'L':
                    nextseats[i] += '#'
                elif c > 0 and inp[i][j] == 'L':
                    nextseats[i] += 'L'
                elif c >= 4 and inp[i][j] == '#':
                    nextseats[i] += 'L'
                elif c < 4 and inp[i][j] == '#':
                    nextseats[i] += '#'
            else:
                nextseats[i] += '.'
    return nextseats

def seatcaller(inp):
    inert = '.' * len(inp[0])
    inp = [ '.' + x + '.' for x in [inert] + inp + [inert]]
    nextseats = []
    while nextseats != inp:
        nextseats = inp
        inp = allseats(inp)
    hashcount = 0
    for x in inp:
        hashcount += x.count('#')
    return hashcount
    

# part 2


def nearseats2(seat, currentinp):
    lookaround = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    c = 0
    for lo in lookaround:
        s = '.'
        lrow = lo[0]
        lcol = lo[1]
        while s == '.':
            if seat[0] + lrow >= 0 and seat[1] + lcol >=0:
                try:
                    s = currentinp[seat[0]+lrow][seat[1]+lcol]
                    lrow += lo[0]
                    lcol += lo[1]
                except IndexError:
                    s = 'X'
            else:
                s = 'X'
        if s == '#':
             c += 1

    return c
        
        


def allseats2(inp):
    nextseats = ['' for _ in range(len(inp))]
    for i in range(len(inp)):
        for j in range(len(inp[i])):
            if inp[i][j] != '.':
                c = nearseats2((i,j),inp)
                if c == 0 and inp[i][j] == 'L':
                    nextseats[i] += '#'
                elif c > 0 and inp[i][j] == 'L':
                    nextseats[i] += 'L'
                elif c >= 5 and inp[i][j] == '#':
                    nextseats[i] += 'L'
                elif c < 5 and inp[i][j] == '#':
                    nextseats[i] += '#'
            else:
                nextseats[i] += '.'
    return nextseats

def seatcaller2(inp):
    nextseats = []
    while nextseats != inp:
        nextseats = inp
        inp = allseats2(inp)
    hashcount = 0
    for x in inp:
        hashcount += x.count('#')
    return hashcount


