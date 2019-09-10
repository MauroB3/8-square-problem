goal = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]]


def find_position_in_goal(n):
    for x in range(0, 3):
        for y in range(0, 3):
            if goal[x][y] == n:
                return x, y


def is_goal(n):
    return n.state == goal

