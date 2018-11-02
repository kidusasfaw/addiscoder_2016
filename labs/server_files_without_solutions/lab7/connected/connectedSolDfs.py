import sys

# This function should take an adjacency list A (a list of lists, where A[i] is a list
# of neighbors of vertex i), and two integers i and j representing two vertices.
def connected(A, i, j):
    # student should implement this function
 
###########################################
# INPUT OUTPUT CODE. DO NOT EDIT CODE BELOW.
n = int(sys.stdin.readline())
for count in range(n):
    v, i, j = tuple(map(int, sys.stdin.readline().split()))
    A = [map(int, sys.stdin.readline().split()) for k in range(v)]
    ans = connected(A, i, j)
    sys.stdout.write(str(ans))
    sys.stdout.write("\n")
sys.stdout.flush()
print ''
