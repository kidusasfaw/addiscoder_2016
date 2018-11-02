import sys

### students should implement numKnightWays

# return the number of ways to get to x,y given that we are currently
# at position (atx, aty)
def knightRecurse(atx, aty, x, y, L, mem):
    if (atx>x) or (aty>y):
        return 0
    elif atx==x and aty==y:
        return 1
    elif mem[atx][aty] != -1:
        return mem[atx][aty]
    mem[atx][aty] = 0
    for t in L:
        mem[atx][aty] += knightRecurse(atx+t[0], aty+t[1], x, y, L, mem)
    return mem[atx][aty]

def numKnightWays(x, y, L):
    mem = []
    for i in xrange(x+1):
        mem += [[-1]*(y+1)]
    return knightRecurse(0, 0, x, y, L, mem)
    	
### DO NOT EDIT ANY CODE BELOW THE LINE ###
x, y, length = tuple(map(int, sys.stdin.readline().split()))
L = [map(int, sys.stdin.readline().split()) for i in range(length)]
ans = numKnightWays(x, y, L)
sys.stdout.write(str(ans))
sys.stdout.flush()
print ''