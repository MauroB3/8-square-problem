from heuristics import goal


def sum_of_wrong_numbers(node):
    result = 0
    for x in range(0, 3):
        for y in range(0, 3):
            if node.get_position(x, y) != goal[x][y]:
                result += 1
    return result

