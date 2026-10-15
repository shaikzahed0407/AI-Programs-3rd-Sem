import heapq

def best_first_search(graph, heuristic, start, goal):
    open_list = []
    heapq.heappush(open_list, (heuristic[start], start))

    visited = set()
    parent = {start: None}

    while open_list:
        h, current = heapq.heappop(open_list)

        if current in visited:
            continue

        print("Visiting:", current)
        visited.add(current)

        if current == goal:
            path = []
            node = goal

            while node is not None:
                path.append(node)
                node = parent[node]

            path.reverse()
            print("Goal found!")
            print("Path:", " -> ".join(path))
            return

        for neighbor in graph[current]:
            if neighbor not in visited and neighbor not in parent:
                parent[neighbor] = current
                heapq.heappush(
                    open_list,
                    (heuristic[neighbor], neighbor)
                )

    print("Goal not found")


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

heuristic = {
    'A': 6,
    'B': 4,
    'C': 3,
    'D': 5,
    'E': 2,
    'F': 1,
    'G': 0
}

best_first_search(graph, heuristic, 'A', 'G')

''' Output:
Visiting: A
Visiting: C
Visiting: G
Goal found!
Path: A -> C -> G
'''