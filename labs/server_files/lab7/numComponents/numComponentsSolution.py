def visit(x, stack, visited):
    visited[x] = True
    stack += [x]

def numComponents(A):
    visited = [False]*len(A)
    ans = 0
    for i in xrange(len(A)):
        if not visited[i]:
            ans += 1
            stack = []
            visit(i, stack, visited)
            while len(stack) > 0:
                x = stack.pop()
                for y in A[x]:
                    if not visited[y]:
                        visit(y, stack, visited)
    return ans

# DO NOT EDIT ANY CODE BELOW THE LINE ###
num_nodes = int(raw_input())
list_graph = []
for i in range(num_nodes):
    nodes = raw_input()
    int_nodes = [int(elem) for elem in nodes.split()]
    list_graph.append(int_nodes)
print numComponents(list_graph)
