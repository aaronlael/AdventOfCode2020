# part 1

def maxseat(inp):
    seats = inp.split('\n')
    maxval = 0
    for seat in seats:
        seatlist = list(seat)
        rows = [x for x in range(0, 128)]
        cols = [x for x in range(0, 8)]
        for r in seatlist[:7]:
            if r == 'F':
                rows = rows[:int(len(rows)/2)]  
            elif r == "B":
                rows = rows[int(len(rows)/2):]
        for c in seatlist[7:]:
            if c == 'L':
                cols = cols[:int(len(cols)/2)]
            elif c == 'R':
                cols = cols[int(len(cols)/2):]
        
        val = rows[0] * 8 + cols[0]
        if val > maxval:
            maxval = val
    return maxval


# part 2

def myseat(inp):
    seats = inp.split('\n')
    occupied = []
    minrow = 128
    maxrow = 0
    for seat in seats:
        seatlist = list(seat)
        rows = [x for x in range(0, 128)]
        cols = [x for x in range(0, 8)]
        for r in seatlist[:7]:
            if r == 'F':
                rows = rows[:int(len(rows)/2)]  
            elif r == "B":
                rows = rows[int(len(rows)/2):]
        for c in seatlist[7:]:
            if c == 'L':
                cols = cols[:int(len(cols)/2)]
            elif c == 'R':
                cols = cols[int(len(cols)/2):]
        occupied += [f"{rows[0]}:{cols[0]}"]
        if rows[0] > maxrow:
            maxrow = rows[0]
        if rows[0] < minrow:
            minrow = rows[0]
    for r in range(minrow +1 ,maxrow):
        for c in range(0,8):
            if f"{r}:{c}" not in occupied:
                return r * 8 + c
