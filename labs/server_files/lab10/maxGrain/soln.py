import sys

def maxGrain(L, W):
    T = []
    for i in xrange(len(L)):
        L[i] = [1.*L[i][0]/L[i][1]] + L[i]
    L.sort()
    L.reverse()
    ans = 0
    for x in L:
        if W == 0:
            break
        ratio = x[0]
        v = x[1]
        w = x[2]
        take = min(w, W)
        ans += ratio*take
        W -= take
    return ans

### DO NOT EDIT ANY CODE BELOW THE LINE ###
N, W = sys.stdin.readline().split(' ')
N = int(N)
W = float(W)
L = []
for i in xrange(N):
  L.append(map(float, sys.stdin.readline().strip().split(' ')))
ans = maxGrain(L, W)
sys.stdout.write(str(ans))
sys.stdout.flush()
print ''
