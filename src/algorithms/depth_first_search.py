from collections import deque


def dfs(graph, initial, is_goal):
    stack = deque()
    visited = set()
    stack.append((initial, []))
    visited.add(initial)
    while stack:
        node, path = stack.pop()
        if is_goal(node):
            return node.state, path, len(path), len(visited)
        for target_node in graph[node]:
            if target_node not in visited:
                visited.add(target_node)
                stack.append((target_node, path + [target_node.last_movement]))
    return None

