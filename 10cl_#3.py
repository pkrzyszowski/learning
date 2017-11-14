import time
x = "   25 23 Sep 2009 system.zip\n 3 14 Aug 2013 to-do-lits.xml\n   44 19 Jun 2013 blockbuster.mpeg  \n      9 12 Dec 2010 notes.html"

def solution(S):
    counter = 0
    splited = [x.strip() for x in S.split('\n')]
    # splited = S.split('\n ')
    for t in splited:
        z = t.split(' ')
        print(z)
        d = z[2] + " " + z[1] + " " + z[3]
        d1 = time.strptime(d, '%b %d %Y')
        if int(z[0]) >= 240*(2^10) and d1 > time.strptime('Jan 31 1990', '%b %d %Y'):
            counter += 1
    if counter > 0:
        return str(counter)
    else:
        return "NO FILES"

print(solution(x))
