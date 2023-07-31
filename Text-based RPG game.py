import random

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage

    def attack(self, enemy):
        damage = random.randint(1, self.attack_power)
        enemy.take_damage(damage)
        print(f"{self.name} attacks {enemy.name} for {damage} damage.")

class Enemy:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage

    def attack(self, player):
        damage = random.randint(1, self.attack_power)
        player.take_damage(damage)
        print(f"{self.name} attacks {player.name} for {damage} damage.")

def get_random_enemy():
    enemies = [
        Enemy("Goblin", 30, 10),
        Enemy("Orc", 50, 15),
        Enemy("Troll", 80, 20),
        Enemy("Dragon", 100, 25),
    ]
    return random.choice(enemies)
def main():
    player_name = input("Enter your name: ")
    player = Player(player_name)

    print(f"Welcome, {player.name}! Let's start the adventure!")

    # Story Introduction
    print("\nYou find yourself in a mysterious forest, far away from home.")
    print("Legend has it that a powerful artifact lies hidden in the depths of this forest, guarded by fearsome creatures.")
    print("Your mission is to find the artifact and bring it back safely.")
    print("Be cautious, as danger lurks behind every tree!")

    while player.is_alive():
        enemy = get_random_enemy()
        print(f"\nA wild {enemy.name} appears!")

        # Battle Loop
        while enemy.is_alive() and player.is_alive():
            action = input("Do you want to attack (a) or run away (r)? ").lower()

            if action == 'a':
                player.attack(enemy)
                if enemy.is_alive():
                    enemy.attack(player)
            elif action == 'r':
                print(f"{player.name} runs away from the {enemy.name}.")
                break
            else:
                print("Invalid choice! Choose 'a' to attack or 'r' to run away.")

        # Check if the player is alive after the battle
        if not player.is_alive():
            print(f"\nOh no, {player.name} has been defeated. The forest claims another victim...")
            break

        # Player wins the battle
        print(f"\nCongratulations! You have defeated the {enemy.name}.")
        print(f"{player.name} finds a potion on the {enemy.name}'s remains and drinks it, restoring some health.")

        # Restore some health after each battle
        player.health += random.randint(10, 20)
        if player.health > 100:
            player.health = 100

    # End of the game
    if player.is_alive():
        print(f"\nCongratulations, {player.name}! You have found the legendary artifact and completed the adventure!")
        print("You are a hero of the forest!")
    else:
        print(f"\nGame over, {player.name}. Your journey ends here. Better luck next time!")

if __name__ == "__main__":
    main()
