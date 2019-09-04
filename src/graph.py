class Graph:

    def __init__(self, first_node):
        self.nodes = {first_node: first_node.get_neighbors()}

    def __getitem__(self, node):
        return node.get_neighbors()
