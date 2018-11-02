import sys

# Students should fill out this function.
def maxGrain(L, W):
  pass

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
