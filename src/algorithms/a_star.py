from queue import PriorityQueue


def a_star(graph, initial, h):
    p_queue = PriorityQueue()
    visited = set()
    p_queue.put((h(initial), initial, []))
    visited.add(initial)
    while not p_queue.empty():
        priority, node, path = p_queue.get_nowait()
        if h(node) == 0:
            return node.state, path, len(path), len(visited)

        for target_node in graph[node]:
            if target_node not in visited:
                visited.add(target_node)
                p_queue.put((
                    priority + h(target_node),
                    target_node,
                    path + [target_node.last_movement]
                ))
    return None
