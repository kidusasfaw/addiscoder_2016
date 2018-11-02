import sys
from collections import deque

# D is the distance to x
def visit(x, queue, distance, D):
    distance[x] = D
    queue += [x]

# returns -1 if there's no path from i to j
# otherwise returns the distance
def distance(A, i, j):
    distance = [-1]*len(A)
    queue = deque()
    visit(i, queue, distance, 0)
    while len(queue) > 0:
        x = queue.popleft()
        if x == j:
            return distance[j]
        for y in A[x]:
            if distance[y] == -1:
                visit(y, queue, distance, distance[x] + 1)
    return -1


### DO NOT EDIT ANY CODE BELOW THE LINE ###
N, M, i, j = map(int, sys.stdin.readline().strip().split(' '))
A = [[] for k in xrange(N)]
for k in xrange(M):
    a, b = map(int, sys.stdin.readline().strip().split(' '))
    A[a].append(b)
ans = distance(A, i, j)
sys.stdout.write(str(ans))
sys.stdout.flush()
print ''
