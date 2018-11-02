import sys
from collections import deque

### students should implement shortestPath
def shortestPath(maze, n, m):
    # student should implement this function
 
###########################################
# INPUT OUTPUT CODE. DO NOT EDIT CODE BELOW.
maze = []
s = sys.stdin.readline().strip().split(' ')
n = int(s[0])
m = int(s[1])
for i in xrange(n):
    maze += [sys.	stdin.readline().strip()]
sys.stdout.write(str(shortestPath(maze, n, m)))
sys.stdout.flush()


