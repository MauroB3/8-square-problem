from node import Node
from graph import Graph
from algorithms.greedy_search import greedy_search
from algorithms.a_star import a_star
from heuristics.sum_of_manhattan_distances import sum_of_manhattan_distances
from heuristics.sum_of_wrong_numbers import sum_of_wrong_numbers

initial_state = [
    [8, 5, 4],
    [7, 6, 3],
    [2, 1, 0]
]

first_node = Node(initial_state)
graph = Graph(first_node)


print("GREEDY SEARCH:")

sown_result, sown_movements = greedy_search(graph, first_node, sum_of_wrong_numbers)

print("Solucion con SOWN")
print("Movimientos: ", len(sown_movements))
print("Solucion: ", sown_movements)

somd_result, somd_movements = greedy_search(graph, first_node, sum_of_manhattan_distances)

print("Solucion con SOMH")
print("Movimientos: ", len(somd_movements))
print("Solucion: ", somd_movements)

print("------------------------------------------------")

print("A STAR:")

sown_result, sown_movements = a_star(graph, first_node, sum_of_wrong_numbers)

print("Solucion con SOWN")
print("Movimientos: ", len(sown_movements))
print("Solucion: ", sown_movements)

somd_result, somd_movements = a_star(graph, first_node, sum_of_manhattan_distances)

print("Solucion con SOMH")
print("Movimientos: ", len(somd_movements))
print("Solucion: ", somd_movements)





