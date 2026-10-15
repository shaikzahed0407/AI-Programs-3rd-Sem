def dfs(graph, start, goal):
    stack = [start]
    visited = set()

    while stack:
        current = stack.pop()

        if current in visited:
            continue

        print("Visiting:", current)
        visited.add(current)

        # Goal test
        if current == goal:
            print("Goal state reached:", goal)
            return True

        # Add unvisited successors to stack
        for neighbour in reversed(graph[current]):
            if neighbour not in visited:
                stack.append(neighbour)

    print("Goal state not found.")
    return False


# State-space representation
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

# Initial and goal states
start_state = 'A'
goal_state = 'G'

# Perform DFS
dfs(graph, start_state, goal_state)

''' Output:
Visiting: A
Visiting: B
Visiting: D
Visiting: E
Visiting: C
Visiting: F
Visiting: G
Goal state reached: G
'''
