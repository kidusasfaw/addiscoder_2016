import sys

def mostActivities(L):
    # student should implement this function
 
###########################################
# INPUT OUTPUT CODE. DO NOT EDIT CODE BELOW.
N = int(sys.stdin.readline())
L = []
for i in xrange(N):
    L.append(map(int, sys.stdin.readline().strip().split(' ')))

ans = mostActivities(L)
sys.stdout.write(str(ans))
sys.stdout.flush()
print ''
