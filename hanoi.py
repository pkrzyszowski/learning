def moveTower(height,fromPole, toPole, withPole):
    if height >= 1:
        print('A')
        print(height)
        moveTower(height-1,fromPole,withPole,toPole)
        print('B')
        moveDisk(fromPole,toPole)
        print('C')
        moveTower(height-1,withPole,toPole,fromPole)

def moveDisk(fp,tp):
    print("moving disk from",fp,"to",tp)

moveTower(3,"1","2","3")