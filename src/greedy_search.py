from queue import PriorityQueue


def gs(graph, initial, h):
    pqueue = PriorityQueue()
    visited = set()
    pqueue.put((h(initial), initial, 0))
    visited.add(initial)
    while not pqueue.empty():
        priority, node, path = pqueue.get_nowait()
        if priority == 0:
            return node, path

        for target_node in graph[node]:
            if target_node not in visited:
                visited.add(target_node)
                pqueue.put((
                    h(target_node),
                    target_node,
                    path + 1
                ))
    print(pqueue.empty())
    return None
