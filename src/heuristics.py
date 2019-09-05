goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]


def h(node):
    result = 0
    for x in range(0, 3):
        for y in range(0, 3):
            if node.get_position(x, y) != goal[x][y]:
                result += 1
    return result

def h2(node):
    result = 0
    flatten_state = [item for sublist in node.state for item in sublist]
    flatten_goal = [item for sublist in goal for item in sublist]
    print(flatten_state, " | ", flatten_goal)
    for x in flatten_state:
        temp = abs(flatten_state.index(x) / 3 - flatten_goal.index(x) / 3)
        print("TEMP: ", temp)
        result += temp
    return result

