from node import Node
from graph import Graph
from greedy_search import gs
from heuristics import h


matrix = [[1, 8, 2],
          [0, 4, 3],
          [7, 6, 5]]

first_node = Node(matrix)

graph = Graph(first_node)

print(gs(graph, first_node, h))

