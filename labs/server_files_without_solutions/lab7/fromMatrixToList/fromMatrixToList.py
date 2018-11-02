def fromMatrixToList():
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
    ans = []
    for i in xrange(len(matrix_graph)):
        ans += [[]]
    for i in xrange(len(matrix_graph)):
        for j in xrange(len(matrix_graph)):
            if matrix_graph[i][j]:
                ans[i] += [j]
    return ans
