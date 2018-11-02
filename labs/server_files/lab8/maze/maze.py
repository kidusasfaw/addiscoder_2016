import sys
from collections import deque

### students should implement shortestPath
def shortestPath(maze, n, m):
    for i in xrange(n):
        for j in xrange(m):
            if maze[i][j] == 'S':
                sx = i
                sy = j
            elif maze[i][j] == 'E':
                ex = i
                ey = j
    # BFS
    distance = []
    for i in xrange(n):
        distance += [[-1]*m]
    queue = deque()
    visit(sx, sy, queue, distance, 0)
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while len(queue) > 0:
        b = queue.popleft()
        x = b[0]
        y = b[1]
        if x==ex and y==ey:
            return distance[x][y]
        # there are at most 4 vertices adjacent to (x,y)
        for i in xrange(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx>=0 and nx<n and ny>=0 and ny<m and maze[nx][ny]!='#':
                if distance[nx][ny] == -1:
                    visit(nx, ny, queue, distance, distance[x][y] + 1)
    if distance[ex][ey] == -1:
        return -1

def visit(x, y, queue, distance, D):
    distance[x][y] = D
    queue += [[x,y]] # push x

### DO NOT EDIT ANY CODE BELOW THE LINE ###
maze = []
s = sys.stdin.readline().strip().split(' ')
n = int(s[0])
m = int(s[1])
for i in xrange(n):
    maze += [sys.	stdin.readline().strip()]
sys.stdout.write(str(shortestPath(maze, n, m)))
sys.stdout.flush()


