def objective(x):
    return -(x - 5) ** 2 + 25

def hill_climbing(start):
    current = start

    while True:
        print("Current state:", current,
              "Value:", objective(current))

        neighbors = [current - 1, current + 1]
        neighbors = [n for n in neighbors if 0 <= n <= 10]

        best_neighbor = max(neighbors, key=objective)

        if objective(best_neighbor) <= objective(current):
            break

        current = best_neighbor

    print("Optimal solution:", current)
    print("Maximum value:", objective(current))

hill_climbing(1)

'''Output:
Current state: 1 Value: 9
Current state: 2 Value: 16
Current state: 3 Value: 21
Current state: 4 Value: 24
Current state: 5 Value: 25
Optimal solution: 5
Maximum value: 25
'''