#6a. Apply Problem Reduction and Means-Ends Analysis techniques to solve AI problems
def problem_reduction(goal):
    problems = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": [],
        "E": [],
        "F": []
    }

    print("Solving:", goal)

    if goal not in problems:
        print("Goal not found")
        return

    if not problems[goal]:
        print(goal, "is solved")
    else:
        print(goal, "is reduced into:", problems[goal])

        for subgoal in problems[goal]:
            problem_reduction(subgoal)

print("Problem Reduction using AND-OR Graph")
problem_reduction("A")

'''
Problem Reduction using AND-OR Graph
Solving: A
A is reduced into: ['B', 'C']
Solving: B
B is reduced into: ['D', 'E']
D is solved
Solving: E
E is solved
Solving: C
C is reduced into: ['F']
Solving: F
F is solved
'''