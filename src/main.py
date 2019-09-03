from node import Node
from graph import Graph
from greedy_search import gs
from heuristics import h


"""
{ 
    [4, 7, 8]
    [5, 1, 3]
    [2, 6, 0] 
}
"""

matrix = [[1, 2, 3], [4, 5, 6], [7, 0, 8]]

first_node = Node(matrix)

graph = Graph(first_node)

print(gs(graph, first_node, h))

