# Braelyn Hewitt-Holbein
# Adventure Game Main Script
# 3-1-26

import gamefunctions

def main():
    # Ask for the player's name
    name = input("Enter your name, adventurer: ")
    
    # Welcome message
    gamefunctions.print_welcome(name, 40)
    
    # Initialize character stats
    character = {'name': name, 'hp': 30, 'gold': 10}
    
    # Main game loop
    while True:
        print("\nYou are in town.")
        print(f"Current HP: {character['hp']}, Current Gold: {character['gold']}")
        
        # Prompt for user action
        choice = gamefunctions.validate_input(
            "What would you like to do?\n"
            "1) Leave town (Fight Monster)\n"
            "2) Sleep (Restore HP for 5 Gold)\n"
            "3) Quit\n",
            ['1', '2', '3']
        )
        
        if choice == '1':
            # Fight a random Shrek-themed monster
            character = gamefunctions.start_fight(character)
        elif choice == '2':
            # Sleep to restore HP for gold
            gamefunctions.sleep(character)
        elif choice == '3':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()