import sys

# Students should fill in this function.
def mostActivities(L):
  pass

### DO NOT EDIT ANY CODE BELOW THE LINE ###
N = int(sys.stdin.readline())
L = []
for i in xrange(N):
    L.append(map(int, sys.stdin.readline().strip().split(' ')))

ans = mostActivities(L)
sys.stdout.write(str(ans))
sys.stdout.flush()
print ''
