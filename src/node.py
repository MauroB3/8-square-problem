import copy


class Node:

    def __init__(self, state):
        self.state = state

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.state == other.state

    def __hash__(self):
        return hash(str(self.state))

    def get_position(self, x, y):
        return self.state[x][y]

    def find_zero_position(self):
        for x in range(0, 3):
            for y in range(0, 3):
                if self.get_position(x, y) == 0:
                    return x, y

    def get_neighbors(self):
        return self.move_up() + self.move_down() + self.move_left() + self.move_right()

    def move_up(self):
        x, y = self.find_zero_position()
        if x != 0:
            result = copy.deepcopy(self.state)
            result[x][y] = self.state[x - 1][y]
            result[x - 1][y] = self.state[x][y]
            return [Node(result)]
        else:
            return []

    def move_down(self):
        x, y = self.find_zero_position()
        if x != 2:
            result = copy.deepcopy(self.state)
            result[x][y] = self.state[x + 1][y]
            result[x + 1][y] = self.state[x][y]
            return [Node(result)]
        else:
            return []

    def move_left(self):
        x, y = self.find_zero_position()
        if y != 0:
            result = copy.deepcopy(self.state)
            result[x][y] = self.state[x][y - 1]
            result[x][y - 1] = self.state[x][y]
            return [Node(result)]
        else:
            return []

    def move_right(self):
        x, y = self.find_zero_position()
        if y != 2:
            result = copy.deepcopy(self.state)
            result[x][y] = self.state[x][y + 1]
            result[x][y + 1] = self.state[x][y]
            return [Node(result)]
        else:
            return []
