from node import Node
from graph import Graph
from algorithms.greedy_search import gs
from heuristics.sum_of_manhattan_distances import sum_of_manhattan_distances

initial_state = [
    [1, 8, 2],
    [0, 4, 3],
    [7, 6, 5]
]

first_node = Node(initial_state)

graph = Graph(first_node)

result, movements = gs(graph, first_node, sum_of_manhattan_distances)

print("Movimientos: ", len(movements))
print(print(movements))



