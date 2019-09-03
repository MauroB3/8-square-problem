matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]


def h(node):
    result = 0
    for x in range(0, 3):
        for y in range(0, 3):
            if node.get_position(x, y) != matrix[x][y]:
                result += 1
    print("Para ", node.state, " la heuristica es ", result)
    return result
