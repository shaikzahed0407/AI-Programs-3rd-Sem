import random
import time


class VacuumEnvironment:

    def __init__(self):
        # Randomly initialize rooms as Clean (0) or Dirty (1)
        self.location_status = {
            "A": random.choice(["Clean", "Dirty"]),
            "B": random.choice(["Clean", "Dirty"]),
        }
        # Randomly place the vacuum agent in Room A or Room B
        self.agent_location = random.choice(["A", "B"])

    def get_percept(self):
        """Returns the current location and status of the room."""
        return self.agent_location, self.location_status[self.agent_location]

    def execute_action(self, action):
        """Changes the environment state based on the agent's action."""
        if action == "Suck":
            self.location_status[self.agent_location] = "Clean"
        elif action == "Move Right" and self.agent_location == "A":
            self.agent_location = "B"
        elif action == "Move Left" and self.agent_location == "B":
            self.agent_location = "A"


class ReflexVacuumAgent:

    def __init__(self):
        self.performance_score = 0

    def program(self, location, status):
        """Reflex logic: Condition-Action Rules"""
        if status == "Dirty":
            print(f"🤖 [Agent]: Found Dirt in Room {location}! Action: Suck")
            self.performance_score += 10  # Reward for cleaning
            return "Suck"
        elif location == "A":
            print(f"🤖 [Agent]: Room A is Clean. Action: Move Right")
            return "Move Right"
        elif location == "B":
            print(f"🤖 [Agent]: Room B is Clean. Action: Move Left")
            return "Move Left"


# --- Execution and Demonstration ---
if __name__ == "__main__":
    # Create environment and agent
    env = VacuumEnvironment()
    agent = ReflexVacuumAgent()

    print("=========================================")
    print("🌍 INITIAL ENVIRONMENT STATE")
    print(f"Room A: {env.location_status['A']}")
    print(f"Room B: {env.location_status['B']}")
    print(f"Starting Agent Location: Room {env.agent_location}")
    print("=========================================\n")

    # Run the agent loop for 3 steps to ensure both rooms are handled
    for step in range(1, 4):
        print(f"--- STEP {step} ---")
        # 1. Agent senses the environment (Perception)
        location, status = env.get_percept()
        print(f"👁️ [Percept]: Currently in Room {location} | Status: {status}")

        # 2. Agent decides action based on rules
        action = agent.program(location, status)

        # 3. Environment changes state
        env.execute_action(action)
        print(f"📉 [Current Score]: {agent.performance_score}\n")
        time.sleep(0.5)

    print("=========================================")
    print("🏆 FINAL SIMULATION SUMMARY")
    print(f"Room A: {env.location_status['A']}")
    print(f"Room B: {env.location_status['B']}")
    print(f"Final Performance Score: {agent.performance_score}")
    print("=========================================")