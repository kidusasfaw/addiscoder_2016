import sys

def maxGrain(L, W):
    # student should implement this function
 
###########################################
# INPUT OUTPUT CODE. DO NOT EDIT CODE BELOW.
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
