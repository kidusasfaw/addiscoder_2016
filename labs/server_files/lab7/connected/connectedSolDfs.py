import sys

### students should implement connected
def visit(x, stack, visited):
    visited[x] = True
    stack += [x]

def connected(A, i, j):
    visited = [False]*len(A)
    stack = []
    visit(i, stack, visited)
    while len(stack) > 0:
        x = stack.pop()
        if x == j:
            return True
        for y in A[x]:
            if not visited[y]:
                visit(y, stack, visited)
    return False

### DO NOT EDIT ANY CODE BELOW THE LINE ###
n = int(sys.stdin.readline())
for count in range(n):
    v, i, j = tuple(map(int, sys.stdin.readline().split()))
    A = [map(int, sys.stdin.readline().split()) for k in range(v)]
    ans = connected(A, i, j)
    sys.stdout.write(str(ans))
    sys.stdout.write("\n")
sys.stdout.flush()
print ''