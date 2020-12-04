"""part 1"""

REQUIRED = ['byr:','iyr:','eyr:','hgt:','hcl:','ecl:','pid:']

def validator1(inp):
    inp = inp.split('\n\n')
    valid = 0
    for passport in inp:
        missing = 0
        for field in REQUIRED:
            if field not in passport:
                missing += 1
        if missing == 0:
            valid += 1
        else:
            missing = 0
    return valid


"""part 2"""

def validator2(inp):
    inp = inp.split('\n\n')
    valid = 0
    for passport in inp:
        passport = passport.replace('\n', ' ').split(' ')
        passdict = { x.split(':')[0] : x.split(':')[1] for x in passport }
        invalid = 0
        # birth year
        byr = ''
        try:
            byr = int(passdict['byr'])
        except (ValueError, KeyError):
            invalid += 1
        if byr == '':
            invalid += 1
        else:
            if byr > 2002:
                invalid += 1
            if byr < 1920:
                invalid += 1
        # issued year
        iyr = ''
        try:
            iyr = int(passdict['iyr'])
        except (ValueError, KeyError):
            invalid += 1
        if iyr == '':
            invalid += 1
        else:
            if iyr < 2010:
                invalid += 1
            if iyr > 2020:
                invalid += 1
        # expiration year
        eyr = ''
        try:
            eyr = int(passdict['eyr'])
        except (ValueError, KeyError):
            invalid += 1
        if eyr == '':
            invalid += 1
        else:
            if eyr < 2020:
                invalid += 1
            if eyr > 2030:
                invalid += 1
        # height
        try:
            if passdict['hgt'][-2:] == 'cm':
                height = int(passdict['hgt'][:-2])
                if height > 193:
                    invalid += 1
                elif height < 150:
                    invalid += 1
            elif passdict['hgt'][-2:] == 'in':
                height = int(passdict['hgt'][:-2])
                if height > 76:
                    invalid += 1
                elif height < 59:
                    invalid +=1
            else:
                invalid += 1
        except (ValueError, KeyError):
            invalid += 1
        # hair color
        colorvals = '0123456789abcdef'
        try:
            haircolor = passdict['hcl']
            hclist = list(haircolor)
            if hclist[0] == '#' and len(hclist) == 7:
                for x in hclist[1:]:
                    if x not in colorvals:
                        invalid += 1
            else:
                invalid += 1
        except KeyError:
            invalid += 1
        # eyecolor
        eyevals = ['amb','blu','brn','gry','grn','hzl','oth']
        try:
            if passdict['ecl'] not in eyevals:
                invalid += 1
        except KeyError:
            invalid += 1
        # passport id
        validpass = '0123456789'
        try:
            if len(passdict['pid']) == 9:
                for n in list(passdict['pid']):
                    if n not in validpass:
                        invalid += 1
            else:
                invalid += 1
        except (KeyError, ValueError):
            invalid += 1
        # am i really valid?
        if invalid == 0:
            valid += 1
    #how many?
    return valid
        

        
