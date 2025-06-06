import time
from pet_logic import Pet

class Game:
    def __init__(self):
        name = input("What would you like to name your pet? ").strip()
        self.pet = Pet(name)

    def start(self):
        print(f"\nWelcome to the pet care game! Your pet's name is {self.pet.name}.", flush=True)
        print(f"{self.pet.name}'s status: Hunger: {self.pet.hunger}, Happiness: {self.pet.happiness}, Energy: {self.pet.energy}\n", flush=True)

        while self.pet.is_alive():
            print("What would you like to do?", flush=True)
            print("1. Feed", flush=True)
            print("2. Play", flush=True)
            print("3. Sleep", flush=True)
            print("4. Check status", flush=True)
            print("5. Quit", flush=True)

            choice = input("> ").strip().lower()

            if choice in ["1", "feed"]:
                self.pet.feed()
            elif choice in ["2", "play"]:
                self.pet.play()
            elif choice in ["3", "sleep"]:
                self.pet.sleep()
            elif choice in ["4", "status", "check status"]:
                self.pet.status()
                continue
            elif choice in ["5", "quit", "exit"]:
                print(f"Goodbye! Thanks for playing with {self.pet.name}.")
                break
            else:
                print(f"Invalid choice: {choice!r}. Try again.")
                continue

            self.pet.pass_time()
            self.pet.status()  # ✅ Show full status after each action
            time.sleep(1)

        else:
            print(f"\nOh no! {self.pet.name} is not doing well and the game is over.")
