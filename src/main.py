from node import Node
from graph import Graph
from algorithms.greedy_search import gs
from heuristics.sum_of_manhattan_distances import sum_of_manhattan_distances
from heuristics.sum_of_wrong_numbers import sum_of_wrong_numbers

initial_state = [
    [1, 0, 2],
    [3, 4, 5],
    [6, 7, 8]
]

first_node = Node(initial_state)
graph = Graph(first_node)

sown_result, sown_movements = gs(graph, first_node, sum_of_manhattan_distances)

print("Solucion con SOWN")
print("Movimientos: ", len(sown_movements))
print("Solucion: ", sown_movements)


somd_result, somd_movements = gs(graph, first_node, sum_of_manhattan_distances)

print("Solucion con SOMH")
print("Movimientos: ", len(somd_movements))
print("Solucion: ", somd_movements)



