# part 1

def questionsum(inp):
    inp = inp.split('\n\n')
    total = 0
    for group in inp:
        group = group.split('\n')
        out = []
        for g in group:
            out += list(g)
        total += len(list(set(out)))
    return total


# part 2

def questionsum2(inp):
    inp = inp.split('\n\n')
    total = 0
    for group in inp:
        group = group.split('\n')
        groupsize = len(group)
        out = []
        for g in group:
            out += list(g)
        groupkey = list(set(out))
        for val in groupkey:
            if out.count(val) == groupsize:
                total += 1     
    return total
