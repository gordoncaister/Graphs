"""
first we need to build graph
by importning our graph class, looping through each ancestor and adding that to the graph

7,4 -- 7,5,4
run depth first traversal. find depth first search returning each result of the dft to the destination node. find the longest dfs value, return the destination of the longest dft (last digit)

"""
import sys
import io
from graph import Graph

def earliest_ancestor(ancestors, starting_node):
    g = Graph()

    for a in ancestors:
        g.add_vertex(a[0])
        g.add_vertex(a[1])
    for a in ancestors:
        g.add_edge(a[1],a[0])

    dft = g.dft(starting_node)
    if len(dft) == 1:
        return -1
    paths = []
    for end in dft:
        paths.append(g.dfs(starting_node,end))
    

    longestpath = []
    longestlength = 0
    for i in range(len(paths)):
        if len(paths[i]) > longestlength:
            print(paths[i])
            longestpath.append(paths[i])
            longestlength = len(paths[i])
        if len(paths[i]) == longestlength:        
            longestpath.append(paths[i])
    
    print(starting_node,longestpath)
    if len(longestpath) == 1:
        print(longestpath[0][-1])
        return(longestpath[0][-1])
    if len(longestpath) == 2:
        print(longestpath)
        return min(longestpath[0][-1],longestpath[1][-1])


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
earliest_ancestor(test_ancestors,8)