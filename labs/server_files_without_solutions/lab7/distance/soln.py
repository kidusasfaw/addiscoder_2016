import sys
from collections import deque

# returns -1 if there's no path from i to j
# otherwise returns the distance
def distance(A, i, j):
    # student should implement this function
 
###########################################
# INPUT OUTPUT CODE. DO NOT EDIT CODE BELOW.
N, M, i, j = map(int, sys.stdin.readline().strip().split(' '))
A = [[] for k in xrange(N)]
for k in xrange(M):
    a, b = map(int, sys.stdin.readline().strip().split(' '))
    A[a].append(b)
ans = distance(A, i, j)
sys.stdout.write(str(ans))
sys.stdout.flush()
print ''
