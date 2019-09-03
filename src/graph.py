class Graph:

    def __init__(self, first_node):
        self.nodes = {first_node: first_node.get_neighbors()}

    def __getitem__(self, item):
        return item.get_neighbors()
