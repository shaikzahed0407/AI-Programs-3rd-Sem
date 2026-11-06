#6b. Apply Problem Reduction and Means-Ends Analysis techniques to solve AI problems
def means_ends_analysis(current, goal):
    print("Current State:", current)

    if current == goal:
        print("Goal Reached!")
        return

    actions = {
        "Start": "Step1",
        "Step1": "Step2",
        "Step2": "Step3",
        "Step3": "Goal"
    }

    if current in actions:
        next_state = actions[current]
        print("Applying action:", current, "->", next_state)
        means_ends_analysis(next_state, goal)
    else:
        print("Goal cannot be reached")

print("Means-Ends Analysis")
means_ends_analysis("Start", "Goal")

'''
Means-Ends Analysis
Current State: Start
Applying action: Start -> Step1
Current State: Step1
Applying action: Step1 -> Step2
Current State: Step2
Applying action: Step2 -> Step3
Current State: Step3
Applying action: Step3 -> Goal
Current State: Goal
Goal Reached!
'''