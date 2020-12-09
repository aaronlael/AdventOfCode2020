import itertools

# part 1

def firstval(inp):
    inp = inp.split('\n')
    for i in range(25, len(inp)+1):
        if int(inp[i]) in [(int(x[0])+int(x[1])) for x in itertools.permutations(inp[i-25:i],2)]:
            continue
        else:
            return inp[i]

# part 2

def weakness(inp):
    inp = inp.split('\n')
    for i in range(len(inp)):
        x = int(inp[i])
        inc = 1
        while x <= 530627549:
            x += int(inp[i+inc])
            if x == 530627549:
                return min([int(x) for x in inp[i:i+inc+1]]) + max([int(x) for x in inp[i:i+inc+1]])
            else:
                inc += 1
            
