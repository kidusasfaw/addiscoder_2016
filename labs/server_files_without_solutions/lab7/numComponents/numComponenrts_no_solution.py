#input
# A : An adjacency list representing the graph. It is a list of lists where the
# first item of the outer list containts the nodes that are adjacent to node zero
# output
# The number of connected components of a graph
def numComponents(A):
    # Your code goes here
    pass

###########################################
# INPUT OUTPUT CODE. DO NOT EDIT CODE BELOW.
num_nodes = int(raw_input())
list_graph = []
for i in range(num_nodes):
    nodes = raw_input()
    int_nodes = [int(elem) for elem in nodes.split()]
    list_graph.append(int_nodes)
print numComponents(list_graph)
