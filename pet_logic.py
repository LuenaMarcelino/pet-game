class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.happiness = 50
        self.energy = 50

    def feed(self):
        self.hunger = max(self.hunger - 20, 0)
        print(f"{self.name} has been fed. Hunger is now {self.hunger}.")

    def play(self):
        if self.energy >= 20:
            self.happiness = min(self.happiness + 20, 100)
            self.energy -= 20
            self.hunger += 10
            print(f"You played with {self.name}. Happiness is now {self.happiness}.")
        else:
            print(f"{self.name} is too tired to play.")

    def sleep(self):
        self.energy = min(self.energy + 40, 100)
        self.hunger += 15
        print(f"{self.name} took a nap. Energy is now {self.energy}.")

    def status(self):
        print(f"\n--- {self.name}'s Status ---")
        print(f"Hunger: {self.hunger}")
        print(f"Happiness: {self.happiness}")
        print(f"Energy: {self.energy}\n")

    def pass_time(self):
        self.hunger = min(self.hunger + 5, 100)
        self.happiness = max(self.happiness - 3, 0)
        self.energy = max(self.energy - 2, 0)

    def is_alive(self):
        return self.hunger < 100 and self.happiness > 0
