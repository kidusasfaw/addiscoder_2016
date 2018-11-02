# inputs
# A : an adjacency list representation of the graph.
# i : The source node
# j : The destination node
# output
# A list containing the node in the path from node i to node j if one exists.
# Otherwise and empty list.
def path(A, i, j):
    # Your code goes here
    pass


###########################################
# INPUT OUTPUT CODE. DO NOT EDIT CODE BELOW.
inp = raw_input()
src,dst = [int(elem) for elem in inp.split()]
num_nodes = int(raw_input())
list_graph = []
for i in range(num_nodes):
    nodes = raw_input()
    int_nodes = [int(elem) for elem in nodes.split()]
    list_graph.append(int_nodes)
print path(list_graph,src,dst)


