from src.node import Node
from src.graph import Graph


"""
{ 
    [4, 7, 8]
    [5, 1, 3]
    [2, 6, 0] 
}
"""

matrix = [[4, 7, 8], [5, 1, 3], [2, 6, 0]]
matrix2 = [[4, 7, 8], [5, 1, 0], [2, 6, 3]]


node = Node(matrix)
node2 = Node(matrix2)
graph = Graph(node)


print(node.__hash__())
print(node2.__hash__())

