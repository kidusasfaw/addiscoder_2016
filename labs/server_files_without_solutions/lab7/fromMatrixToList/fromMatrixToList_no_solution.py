#input
# A : An adjacency matrix representing the graph. It is a list of lists where the
# first item of the outer list contains zeros and ones representing if node zero
# has connections to node 0,1,2 and so on.
# output
# An adjacency list representation of the graph as a list of lists.
def fromMatrixToList(A):
    # Your code goes here
    pass

###########################################
# INPUT OUTPUT CODE. DO NOT EDIT CODE BELOW.
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
