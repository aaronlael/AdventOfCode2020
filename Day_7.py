
# part 1

def goldbag(inp):
    rules = inp.split('\n')
    dictrules = {}
    for rule in rules:
        vals = rule.split(" contain ")
        key = ' '.join(vals[0].split(" ")[:-1])
        contents = vals[1].split(', ')
        dictrules[key] = []
        if contents != 'no other': 
            for content in contents:
                dictrules[key] += [' '.join(content.split(' ')[1:-1])]
        bagcount = 0
        goldbags = ['shiny gold']
        while len(goldbags) != bagcount:
            bagcount = len(goldbags)
            for key in dictrules.keys():
                for bag in goldbags:
                    if bag in dictrules[key]:
                        goldbags += [key]
            goldbags = list(set(goldbags))
    # subtract 1 for shiny gold bag itself
    return bagcount - 1

# part 2

def goldcount(inp):
    rules = inp.split('\n')
    dictrules = {}
    for rule in rules:
        vals = rule.split(' contain ')
        key = ' '.join(vals[0].split(' ')[:-1])
        contents = vals[1].split(', ')
        dictrules[key] = []
        if 'no other bags.' not in contents: 
            for content in contents:
                dictrules[key] += [' '.join(content.split(' ')[:-1])]
    baglist = ['shiny gold']
    bagcount = 0
    while len(baglist) > 0:
        nextbags = dictrules[baglist[0]]
        for bag in nextbags:
            if len(bag) > 0:
                bc = int(bag.split(' ')[0])
                b = ' '.join(bag.split(' ')[1:])
                baglist += bc * [b]
        baglist = baglist[1:]
        bagcount += 1
    return bagcount - 1             
        
        
    
                
