import random
import tkinter as tk
from tkinter import messagebox

class Player:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.max_health = 100
        self.health = self.max_health
        self.attack_power = 20
        self.gold = 0

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage

    def attack(self, enemy):
        damage = random.randint(1, self.attack_power)
        enemy.take_damage(damage)
        print(f"{self.name} attacks {enemy.name} for {damage} damage.")

    def level_up(self):
        print(f"{self.name} leveled up to level {self.level}!")
        print(f"{self.name}'s attributes have improved. Choose one attribute to increase:")
        print("1. Max Health (+20 health)")
        print("2. Attack Power (+5 attack power)")
        print("3. Gold (+50 gold)")
        choice = input("Enter the option number: ")

        if choice == '1':
            self.health +=20
        elif choice == '2':
            self.attack_power += 5
        elif choice == '3':
            self.gold += 50
        else:
            print("Invalid choice! Defaulting to increasing max health.")
            self.health +=20

        self.health = self.max_health

    def display_attributes(self):
        print(f"Name: {self.name} | Level: {self.level} | Health: {self.health}/{self.max_health} | Attack Power: {self.attack_power} | Gold: {self.gold}")

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

class NPC:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def give_quest(self, player):
        pass

class WizardNPC(NPC):
    def give_quest(self, player):
        print(f"\nHello, {player.name}! I am {self.name}, the wizard.")
        print("I will grant you a powerful spell if you can bring me 3 magical crystals.")
        print("Magical crystals can be found in the deeper parts of the forest, guarded by strong creatures.")

        if input("Do you accept the quest to find 3 magical crystals? (yes/no): ").lower() == 'yes':
            player.quest = "crystals"
            print("Good luck on your quest!")

class AlchemistNPC(NPC):
    def give_quest(self, player):
        print(f"\nGreetings, {player.name}! I am {self.name}, the alchemist.")
        print("I can brew a potent healing potion, but I need some rare ingredients.")
        print("To create the potion, bring me 5 sparkling mushrooms found near the riverbank.")

        if input("Do you accept the quest to find 5 sparkling mushrooms? (yes/no): ").lower() == 'yes':
            player.quest = "mushrooms"
            print("Best of luck on your quest!")

def get_random_enemy(level):
    base_health = 30 + (level - 1) * 20
    base_attack_power = 10 + (level - 1) * 5

    name = random.choice(["Goblin", "Orc", "Troll", "Dragon"])
    health = random.randint(base_health - 10, base_health + 10)
    attack_power = random.randint(base_attack_power - 3, base_attack_power + 3)

    return Enemy(name, health, attack_power)

def choose_attack_option():
    print("\nChoose your attack option:")
    print("1. Attack with a sword (High damage, medium success rate)")
    print("2. Cast a spell (Medium damage, high success rate)")
    print("3. Use a bow and arrow (Low damage, low success rate)")
    choice = input("Enter the option number: ")

    if choice == '1':
        return "sword"
    elif choice == '2':
        return "spell"
    elif choice == '3':
        return "bow"
    else:
        print("Invalid choice! Defaulting to attack with a sword.")
        return "sword"

def attack_with_sword(player, enemy):
    damage = random.randint(15, 25)
    enemy.take_damage(damage)
    print(f"{player.name} attacks {enemy.name} with a sword for {damage} damage.")

def cast_spell(player, enemy):
    damage = random.randint(5, 20)
    enemy.take_damage(damage)
    print(f"{player.name} casts a spell on {enemy.name} for {damage} damage.")

def use_bow(player, enemy):
    damage = random.randint(10, 15)
    enemy.take_damage(damage)
    print(f"{player.name} shoots an arrow at {enemy.name} for {damage} damage.")

def main():
    player_name = input("Enter your name: ")
    player = Player(player_name)

    print(f"Welcome, {player.name}! Let's start the adventure!")

    # Story Introduction
    print("\nYou find yourself in a mysterious forest, far away from home.")
    print("Legend has it that a powerful artifact lies hidden in the depths of this forest, guarded by fearsome creatures.")
    print("Your mission is to find the artifact and bring it back safely.")
    print("Be cautious, as danger lurks behind every tree!")
    
    wizard_npc = WizardNPC("Gandalf", "a wise wizard")
    alchemist_npc = AlchemistNPC("Merlin", "a powerful alchemist")

    level = 1
    while player.is_alive() and level <= 4:
                # Story choices
        if level == 2:
            choice = input("\nYou come across a hidden path. Do you want to explore it? (y/n): ").lower()
            if choice == 'y':
                print("\nYou find a treasure chest filled with gold coins!")
                print("\n(+50 gold coins)")
                player.gold += 50
            else:
                print("\nYou decide to continue on the main path.")

        if level == 3:
            choice = input("\nYou encounter a group of travelers. Do you want to join them? (y/n): ").lower()
            if choice == 'y':
                print("\nYou join the travelers and embark on an epic journey together.")
                print("They share valuable knowledge and teach you new combat skills!")
                player.attack_power += 5
                print("(+5 attack power)")
            else:
                print("\nYou decide to continue your quest alone.")

        if level == 4:
            choice = input("\nYou find an ancient shrine. Do you want to pray to the gods? (y/n): ").lower()
            if choice == 'y':
                print("\nThe gods are pleased with your devotion and grant you a divine blessing.")
                print("Your health is fully restored, and you feel invigorated!")
                player.health = player.max_health
            else:
                print("\nYou decide to continue without seeking divine aid.")

        print(f"\n--- Level {level} ---")
        print("You venture deeper into the forest...")
        
        # Level challenges (customize as needed)
        num_enemies =  4 #random.randint(2, 4)
        action = [0,1,2,3]
        for i in range(num_enemies):
            enemy = get_random_enemy(level)
            print(f"\nA wild {enemy.name} appears!")

            while enemy.is_alive() and player.is_alive():
                
                action[i-1] = input("Do you want to attack (a) or run away (r)? ").lower()

                if action == 'a':
                    attack_option = choose_attack_option()
                    if attack_option == "sword":
                        attack_with_sword(player, enemy)
                    elif attack_option == "spell":
                        cast_spell(player, enemy)
                    elif attack_option == "bow":
                        use_bow(player, enemy)
                    else:
                        print("Invalid choice! Defaulting to attack with a sword.")

                    if enemy.is_alive():
                        enemy.attack(player)
                elif action == 'r':
                    print(f"{player.name} runs away from the {enemy.name}.")
                    break
                else:
                    print("Invalid choice! Choose 'a' to attack or 'r' to run away.")

        if not player.is_alive():
            print(f"\nOh no, {player.name} has been defeated. The forest claims another victim...")
            break
        
        # Task to obtain the spell
        if level == 3 and player.quest is None:
            wizard_npc.give_quest(player)

        # Task to obtain the potions
        if level == 4 and player.quest is None:
            alchemist_npc.give_quest(player)
        

        print(f"\nCongratulations! You have completed Level {level}.")
        print(f"{player.name} finds a potion and drinks it, restoring some health.")
        health_regain = random.randint(10, 20)
        player.health += health_regain
        print(f"+ {health_regain} healthpoints")
        if player.health > player.max_health:
            player.health = player.max_health

        if level < 4:
            print(f"\n{player.name}, you've reached the end of Level {level}.")
            print("You have the opportunity to level up and improve your attributes!")
            player.level_up()

        player.display_attributes()

        level += 1

    if player.is_alive() and level > 4:
        print(f"\nCongratulations, {player.name}! You have found the legendary artifact and completed the adventure!")
        print("You are a hero of the forest!")
    else:
        print(f"\nGame over, {player.name}. Your journey ends here. Better luck next time!")

if __name__ == "__main__":
    main()


#######################################################################

class GameGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Adventure Game")
        self.player = None
        self.level = 1
        self.create_player()

    def create_player(self):
        self.player_name_label = tk.Label(self.root, text="Enter your name:")
        self.player_name_label.pack()

        self.player_name_entry = tk.Entry(self.root)
        self.player_name_entry.pack()

        self.submit_button = tk.Button(self.root, text="Start", command=self.start_game)
        self.submit_button.pack()

    def start_game(self):
        player_name = self.player_name_entry.get()
        self.player = Player(player_name)

        self.player_name_label.destroy()
        self.player_name_entry.destroy()
        self.submit_button.destroy()

        self.start_adventure()

    def start_adventure(self):
        self.welcome_label = tk.Label(self.root, text=f"Welcome, {self.player.name}! Let's start the adventure!")
        self.welcome_label.pack()

        self.intro_label = tk.Label(self.root, text="You find yourself in a mysterious forest, far away from home.")
        self.intro_label.pack()
        # ... (unchanged)

        self.level = 1
        while self.player.is_alive() and self.level <= 4:
            self.play_level()

            if not self.player.is_alive():
                messagebox.showinfo("Defeat", f"Oh no, {self.player.name} has been defeated. The forest claims another victim...")
                break

            # Player wins the level
            messagebox.showinfo("Level Complete", f"Congratulations! You have completed Level {self.level}.")
            self.player.health += random.randint(20, 30)
            if self.player.health > self.player.max_health:
                self.player.health = self.player.max_health

            if self.level < 4:
                self.level_up()

            self.display_attributes()

            self.level += 1

        # End of the game
        if self.player.is_alive() and self.level > 4:
            messagebox.showinfo("Congratulations", f"Congratulations, {self.player.name}! You have found the legendary artifact and completed the adventure!")
            messagebox.showinfo("Congratulations", "You are a hero of the forest!")
        else:
            messagebox.showinfo("Game Over", f"Game over, {self.player.name}. Your journey ends here. Better luck next time!")

    def play_level(self):
        level_window = tk.Toplevel(self.root)
        level_window.title(f"Level {self.level}")

        level_label = tk.Label(level_window, text=f"--- Level {self.level} ---\nYou venture deeper into the forest...")
        level_label.pack()

        # Level challenges (customize as needed)
        for _ in range(random.randint(2, 4)):
            enemy = get_random_enemy(self.level)
            enemy_label = tk.Label(level_window, text=f"\nA wild {enemy.name} appears!")
            enemy_label.pack()

            while enemy.is_alive() and self.player.is_alive():
                action = self.choose_action(level_window)

                if action == 'attack':
                    attack_option = self.choose_attack_option(level_window)
                    if attack_option == "sword":
                        attack_with_sword(self.player, enemy)
                    elif attack_option == "spell":
                        cast_spell(self.player, enemy)
                    elif attack_option == "bow":
                        use_bow(self.player, enemy)
                    else:
                        print("Invalid choice! Defaulting to attack with a sword.")

                    if enemy.is_alive():
                        enemy.attack(self.player)
                elif action == 'run':
                    print(f"{self.player.name} runs away from the {enemy.name}.")
                    break
                else:
                    print("Invalid choice! Choose 'attack' to attack or 'run' to run away.")

            if not self.player.is_alive():
                messagebox.showinfo("Defeat", f"Oh no, {self.player.name} has been defeated. The forest claims another victim...")
                level_window.destroy()
                break

        level_window.destroy()

    def choose_action(self, level_window):
        response = messagebox.askyesno("Action", "Do you want to attack?")
        if response:
            return 'attack'
        else:
            return 'run'

    def choose_attack_option(self, level_window):
        response = messagebox.askyesno("Attack Option", "Choose your attack option:\n1. Attack with a sword (High damage, medium success rate)\n2. Cast a spell (Medium damage, high success rate)\n3. Use a bow and arrow (Low damage, low success rate)")
        if response:
            choice = messagebox.askinteger("Choose Option", "Enter the option number:")
            if choice == 1:
                return "sword"
            elif choice == 2:
                return "spell"
            elif choice == 3:
                return "bow"
            else:
                messagebox.showinfo("Invalid Choice", "Invalid choice! Defaulting to attack with a sword.")
                return "sword"
        else:
            return "sword"

    def level_up(self):
        response = messagebox.askyesno("Level Up", f"{self.player.name}, you've reached the end of Level {self.level}.\nYou have the opportunity to level up and improve your attributes!\nDo you want to level up?")
        if response:
            improvement_choice = messagebox.askinteger("Attribute Improvement", f"Choose one attribute to increase:\n1. Max Health (+20 health)\n2. Attack Power (+5 attack power)\n3. Gold (+50 gold)")
            if improvement_choice == 1:
                self.player.max_health += 20
                self.player.health = self.player.max_health
            elif improvement_choice == 2:
                self.player.attack_power += 5
            elif improvement_choice == 3:
                self.player.gold += 50
            else:
                messagebox.showinfo("Invalid Choice", "Invalid choice! Defaulting to increasing max health.")
                self.player.max_health += 20
                self.player.health = self.player.max_health

    def display_attributes(self):
        attributes = f"Name: {self.player.name} | Level: {self.player.level} | Health: {self.player.health}/{self.player.max_health} | Attack Power: {self.player.attack_power} | Gold: {self.player.gold}"
        messagebox.showinfo("Player Attributes", attributes)


if __name__ == "__main__":
    game_gui = GameGUI()
    game_gui.root.mainloop()
