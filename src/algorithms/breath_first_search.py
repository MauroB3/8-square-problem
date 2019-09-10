from collections import deque


def bfs(graph, initial, is_goal):
    queue = deque()
    visited = set()
    queue.append((initial, []))
    visited.add(initial)
    while queue:
        node, path = queue.popleft()
        if is_goal(node):
            return node.state, path, len(path), len(visited)
        for target_node in graph[node]:
            if target_node not in visited:
                visited.add(target_node)
                queue.append((target_node, path + [target_node.last_movement]))
    return None

