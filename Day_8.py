# part 1

def laststep(inp):
    inp = inp.split('\n')
    acc = 0
    location = [0]
    endwhile = 0
    while endwhile == 0:
        row = inp[location[-1]].split(' ')
        if row[0] == 'acc':
            if row[1][0] == '+':
                acc += int(row[1][1:])
            else:
                acc -= int(row[1][1:])   
            nextloc = location[-1]+1
        elif row[0] == 'jmp':
            if row[1][0] == '+':
                nextloc = location[-1] + int(row[1][1:])
            else:
                nextloc = location[-1] - int(row[1][1:])
        else:
            nextloc = location[-1]+1
        if nextloc in location:
            endwhile += 1
        else:
            location += [nextloc]
    return acc


# part 2

def laststep2(inp):
    if type(inp) != type([]):
        inp = inp.split('\n')
    acc = 0
    location = [0]
    endwhile = 0
    endloc = len(inp)
    reason = ''
    while endwhile == 0:
        row = inp[location[-1]].split(' ')
        if row[0] == 'acc':
            if row[1][0] == '+':
                acc += int(row[1][1:])
            else:
                acc -= int(row[1][1:])   
            nextloc = location[-1]+1
        elif row[0] == 'jmp':
            if row[1][0] == '+':
                nextloc = location[-1] + int(row[1][1:])
            else:
                nextloc = location[-1] - int(row[1][1:])
        else:
            nextloc = location[-1]+1
        if nextloc in location:
            endwhile += 1
            reason = 'loop'
        else:
            location += [nextloc]
        if endloc in location:
            endwhile += 1
            reason = 'end'
    return acc, location, reason

def rightstep(inp):
    steps = laststep2(inp)[1]
    inp = inp.split('\n')
    for step in steps:
        if  inp[step].split(' ')[0] == 'acc':
            continue
        else:
            if inp[step].split(' ')[0] == 'nop':
                newinp = inp[:step] + [(f"jmp {inp[step].split(' ')[-1]}")] + inp[step+1:]
            else:
                newinp = inp[:step] + [(f"nop {inp[step].split(' ')[-1]}")] + inp[step+1:]
            acc, loc, reason = laststep2(newinp)
            if reason== 'end':
                return acc
            
            
    
    


        
        

