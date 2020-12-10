# part 1

def outletchain(inp):
    inp  = sorted([int(x) for x in inp.split('\n')])
    inp = [0] + inp + [max(inp) + 3]
    oneoff = 0
    threeoff = 0
    for i in range(len(inp) - 1):
        if inp[i+1] - inp[i] == 1:
            oneoff += 1
        else:
            threeoff += 1
    return threeoff * oneoff
        
    

# part 2
"""I tried to brute force this with itertools.combinations at first, then went
to the subreddit and got pointers on a more mathematical solution"""

def gaps(inp):
    inp  = sorted([0] + [int(x) for x in inp.split('\n')])
    gapped = []
    pos = 0
    for i in range(1,len(inp)):
        if inp[i] - inp[i-1] == 1:
            if i == len(inp)-1:
              gapped += [inp[pos:i+1]]
            continue
        else:
            gapped += [inp[pos:i]]
            pos = i
    fivecount = 0
    fourcount = 0
    threecount = 0
    for x in gapped:
        if len(x) == 5:
            fivecount += 1
        elif len(x) == 4:
            fourcount += 1
        elif len(x) == 3:
            threecount += 1
        else:
            continue
        
    return 2**threecount * 4**fourcount * 7**fivecount
        
    

