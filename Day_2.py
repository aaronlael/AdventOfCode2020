"""part 1"""


def invalid(pw):
    pw = pw.split('\n')
    pwlen = len(pw)
    invalid = 0

    for x in pw:
        r, c, p = x.split(' ')
        rstart, rend = r.split('-')
        c = c.split(':')[0]
        if p.count(c) < int(rstart) or p.count(c) > int(rend):
            invalid +=1

    print(pwlen - invalid)



"""part 2"""

def valid(pw):
    pw = pw.split('\n')
    valid = 0
    for x in pw:
        r, c, p = x.split(' ')
        rstart, rend = r.split('-')
        c = c.split(':')[0]
        if (c == p[int(rstart)-1] and c != p[int(rend)-1]) or (c == p[int(rend)-1] and c != p[int(rstart)-1]):
            valid += 1

    print(valid)
