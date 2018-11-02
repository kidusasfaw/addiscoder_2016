import sys

### students should implement image here
def dfs(x, y, visited, image):
	dx = [1, -1, 0, 0]
	dy = [0, 0, 1, -1]
	n = len(image)
	m = len(image[0])
	visited[x][y] = True
	ans = 1
	for i in xrange(4):
		nx = x + dx[i]
		ny = y + dy[i]
		if nx>=0 and nx<n and ny>=0 and ny<m and image[x][y]==image[nx][ny]:
			if not visited[nx][ny]:
				ans += dfs(nx, ny, visited, image)
	return ans


def largestObjInImage(image):
	n = len(image)
	m = len(image[0])
	visited = []
	for i in xrange(n):
		visited += [[False]*m]
	ans = 0
	for i in xrange(n):
		for j in xrange(m):
			if not visited[i][j]:
				ans = max(ans, dfs(i, j, visited, image))
	return ans

### DO NOT EDIT ANY CODE BELOW THE LINE ###
dim = sys.stdin.readline().strip().split(' ')
n = int(dim[0])
m = int(dim[1])
image = []
for i in xrange(n):
	image += [sys.stdin.readline().strip().split(' ')]
ans = largestObjInImage(image)
sys.stdout.write(str(ans))
print ''

