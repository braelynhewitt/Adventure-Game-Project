# Braelyn Hewitt-Holbein
# Adventure Game Main Script
# 3-1-26

import gamefunctions

def main():
    # Ask for the player's name
    name = input("Enter your name, adventurer: ")
    
    # Welcome message
    gamefunctions.print_welcome(name, 40)
    
    # Show the shop menu
    gamefunctions.print_shop_menu("Sword", 10, "Potion", 5)
    
    # Example purchase
    can_buy, money_left = gamefunctions.purchase_item(5, 15, 2)
    print(f"\nYou bought {can_buy} items and have ${money_left} left.\n")
    
    # Generate a random monster
    monster = gamefunctions.new_random_monster()
    print(f"A wild {monster['name']} appears!")
    print(f"Description: {monster['description']}")
    print(f"Health: {monster['health']}, Power: {monster['power']}, Money: {monster['money']}")

if __name__ == "__main__":
    main()
