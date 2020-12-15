# part 1

def shuttle(inp):
    val = int(inp[0])
    buses = [int(x) for x in inp[1].split(',') if x != 'x']
    out = { 'bus' : 0, 'time' : val}
    while out['bus'] == 0:
        for bus in buses:
            if divmod(out['time'], bus)[1] == 0:
                out['bus'] = bus
                break
        else:
            out['time'] += 1
    return (out['time'] - val) * out['bus']
    
    

# part 2

# does not run in time
def goldshuttle(inp):
    inp = [(x[0], int(x[1])) for x in enumerate(inp[1].split(',')) if x[1] != 'x']
    interval = sorted([(x[0], int(x[1])) for x in enumerate(inp[1].split(',')) if x[1] != 'x'], key=lambda x:x[1], reverse=True)[0][1]
    for v in inp:
        if v[1] == interval:
            timestamp = interval - v[0]
            break
    success = 0
    while success == 0:
        for v in inp:
            if divmod(timestamp + v[0], v[1])[1] != 0:
                timestamp += interval
                break
        else:
            success = 1
    return timestamp

        

# inp
inp = """1015292
19,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,743,x,x,x,x,x,x,x,x,x,x,x,x,13,17,x,x,x,x,x,x,x,x,x,x,x,x,x,x,29,x,643,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,23""".split('\n')

miniinp = """939
7,13,x,x,59,x,31,19""".split('\n')
