# part 1

def goldbag(inp):
    rules = inp.split('\n')
    dictrules = {}
    for rule in rules:
        vals = rule.split(" contain ")
        key = vals[0]
        contents = vals[1].split(', ')
        dictrules[key] = []
        if contents != 'no other bags': 
            for content in contents:
                dictrules[key] += [' '.join(content.split(' ')[1:-1])]
    goldbags = ['shiny gold']                            
    goldcount = 0
    for key in dictrules.keys():
        for bag in goldbags:
            if bag in dictrules[key]:
                goldbags += [bag]

    return goldbags                
        
        
    
                
