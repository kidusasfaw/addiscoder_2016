
def fromListToMatrix():
    num_nodes = int(raw_input())
    list_graph = []
    for i in range(num_nodes):
        nodes = raw_input()
        int_nodes = [int(elem) for elem in nodes.split()]
        list_graph.append(int_nodes)
        print list_graph
    ans = []
    for i in xrange(len(list_graph)):
        ans += [[0]*len(list_graph)]
    for i in xrange(len(list_graph)):
        for x in list_graph[i]:
            ans[i][x] = 1
    return ans

### DO NOT EDIT ANY CODE BELOW THE LINE ###
num_nodes = int(raw_input())
list_graph = []
for i in range(num_nodes):
    nodes = raw_input()
    int_nodes = [int(elem) for elem in nodes.split()]
    list_graph.append(int_nodes)
print fromListToMatrix(list_graph)
    

