def fromListToMatrix(A):
    # student should implement this function
 
###########################################
# INPUT OUTPUT CODE. DO NOT EDIT CODE BELOW.
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
