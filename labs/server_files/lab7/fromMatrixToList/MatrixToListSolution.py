def fromMatrixToList(A):
    ans = []
    for i in xrange(len(A)):
        ans += [[]]
    for i in xrange(len(A)):
        for j in xrange(len(A)):
            if A[i][j]:
                ans[i] += [j]
    return ans

### DO NOT EDIT ANY CODE BELOW THE LINE ###
num_nodes = int(raw_input())
matrix_graph = []
for i in range(num_nodes):
    nodes = raw_input()
    int_nodes = [int(elem) for elem in nodes.split()]
    if len(int_nodes) != num_nodes:
        sys.stderr.write("You must have "+str(num_nodes) + " entries per node")
        std.stderr.flush()
        return
    matrix_graph.append(int_nodes)
    print matrix_graph

print fromMatrixToList(matrix_graph)
