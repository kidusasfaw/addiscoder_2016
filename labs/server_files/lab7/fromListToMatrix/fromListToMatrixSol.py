def fromListToMatrix(A):
    ans = []
    for i in xrange(len(A)):
        ans += [[0]*len(A)]
    for i in xrange(len(A)):
        for x in A[i]:
            ans[i][x] = 1
    return ans

### DO NOT EDIT ANY CODE BELOW THE LINE ###
num_nodes = int(raw_input())
list_graph = []
for i in range(num_nodes):
    try :
        nodes = raw_input()
        int_nodes = [int(elem) for elem in nodes.split()]
        list_graph.append(int_nodes)
    except (EOFError):
        empty_lists_remaining = num_nodes - len(list_graph)
        for x in range(empty_lists_remaining):
            list_graph.append([])

print fromListToMatrix(list_graph)
