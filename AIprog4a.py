import random

def generate_and_test():
    target = 7
    attempts = 0

    while True:
        number = random.randint(1, 10)
        attempts += 1

        print("Generated number:", number)

        if number == target:
            print("Solution found:", number)
            print("Attempts:", attempts)
            break

generate_and_test()

'''Output:
Generated number: 7
Solution found: 7
Attempts: 1
'''