import sys

def mostActivities(L):
    for x in L:
        x[0],x[1] = x[1],x[0]
    L.sort()
    for x in L:
        x[0],x[1] = x[1],x[0]

    ans = 1
    last = L[0][1]
    for x in L:
        if x[0] < last:
            continue
        else:
            ans += 1
            last = x[1]
    return ans

### DO NOT EDIT ANY CODE BELOW THE LINE ###
N = int(sys.stdin.readline())
L = []
for i in xrange(N):
    L.append(map(int, sys.stdin.readline().strip().split(' ')))

ans = mostActivities(L)
sys.stdout.write(str(ans))
sys.stdout.flush()
print ''
