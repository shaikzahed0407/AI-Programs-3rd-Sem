from collections import deque

def bfs(graph, start, goal):
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        current, path = queue.popleft()

        if current == goal:
            return path

        if current not in visited:
            visited.add(current)

            for neighbor in graph.get(current, []):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

    return None


# State-space representation
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': ['H'],
    'F': [],
    'G': ['H'],
    'H': []
}

start = 'A'
goal = 'H'

result = bfs(graph, start, goal)

if result:
    print("Path found using BFS:")
    print(" -> ".join(result))
else:
    print("Goal state cannot be reached.")