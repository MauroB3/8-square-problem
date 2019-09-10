from node import Node
from graph import Graph
from algorithms.depth_first_search import dfs
from algorithms.breath_first_search import bfs
from algorithms.a_star import a_star
from algorithms.greedy_search import greedy_search
from heuristics.sum_of_manhattan_distances import sum_of_manhattan_distances
from heuristics.sum_of_wrong_numbers import sum_of_wrong_numbers
from heuristics.goal import goal, is_goal

initial_state = [
    [1, 2, 3],
    [6, 0, 7],
    [5, 8, 4]
]

first_node = Node(initial_state)
graph = Graph(first_node)

print("Estado inicial:")
print("     ", initial_state[0])
print("     ", initial_state[1])
print("     ", initial_state[2], "\n")

print("------------------------------------------------", "\n")

print("GREEDY SEARCH:", "\n")

sown_result, sown_solution, sown_movements, sown_visited = greedy_search(graph, first_node, sum_of_wrong_numbers)

print("Solucion con SOWN")
print("Nodos explorados: ", sown_visited)
print("Movimientos: ", sown_movements)
print("Solucion: ", sown_solution, "\n")

somd_result, somd_solution, somd_movements, somd_visited = greedy_search(graph, first_node, sum_of_manhattan_distances)

print("Solucion con SOMD")
print("Nodos explorados: ", somd_visited)
print("Movimientos: ", somd_movements)
print("Solucion: ", somd_solution, "\n")

print("------------------------------------------------", "\n")

print("A STAR:", "\n")

sown_result, sown_solution, sown_movements, sown_visited = a_star(graph, first_node, sum_of_wrong_numbers)

print("Solucion con SOWN")
print("Nodos explorados: ", sown_visited)
print("Movimientos: ", sown_movements)
print("Solucion: ", sown_solution, "\n")

somd_result, somd_solution, somd_movements, somd_visited = a_star(graph, first_node, sum_of_manhattan_distances)

print("Solucion con SOMD")
print("Nodos explorados: ", somd_visited)
print("Movimientos: ", somd_movements)
print("Solucion: ", somd_solution)

print("------------------------------------------------", "\n")

bfs_result, bfs_solution, bfs_movements, bfs_visited = bfs(graph, first_node, is_goal)

print("BREATH FIRST SEARCH:", "\n")

print("Nodos explorados: ", bfs_visited)
print("Movimientos: ", bfs_movements)
print("Solucion: ", bfs_solution)

print("------------------------------------------------", "\n")

dfs_result, dfs_solution, dfs_movements, dfs_visited = dfs(graph, first_node, is_goal)

print("DEPTH FIRST SEARCH:", "\n")

print("Nodos explorados: ", dfs_visited)
print("Movimientos: ", dfs_movements)
print("Solucion: ", dfs_solution)







