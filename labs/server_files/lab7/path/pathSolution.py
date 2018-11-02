def visit(x, last, stack, visited, previous):
    visited[x] = True
    previous[x] = last
    stack += [x]




def path(A, i, j):
    visited = [False]*len(A)
    # previous[k] is the vertex right before k on a path from i to k
    previous = [-1]*len(A)
    stack = []
    visit(i, -1, stack, visited, previous)
    while len(stack) > 0:
        x = stack.pop()
        if x == j:
            ans = [j]
            while ans[len(ans)-1] != i:
                ans += [previous[ans[len(ans)-1]]]
            ans.reverse()
            return ans
        for y in A[x]:
            if not visited[y]:
                visit(y, x, stack, visited, previous)
    return []


# DO NOT EDIT ANY CODE BELOW THE LINE ###
inp = raw_input()
src,dst = [int(elem) for elem in inp.split()]
num_nodes = int(raw_input())
list_graph = []
for i in range(num_nodes):
    nodes = raw_input()
    int_nodes = [int(elem) for elem in nodes.split()]
    list_graph.append(int_nodes)
print path(list_graph,src,dst)

