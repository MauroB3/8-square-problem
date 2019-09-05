from heuristics.goal import goal
from heuristics.goal import find_position_in_goal


def sum_of_manhattan_distances(node):
    result = 0
    for x in range(0, 3):
        for y in range(0, 3):
            number = node.get_position(x, y)
            if number != goal[x][y]:
                x_goal, y_goal = find_position_in_goal(number)
                result += abs((x + y) - (x_goal + y_goal))
    return result

