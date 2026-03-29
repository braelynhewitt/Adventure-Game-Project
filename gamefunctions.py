# Braelyn Hewitt-Holbein
# Updated Game functions
# 3-1-26

"""
gamefunctions.py contains core functions for an adventure game.

This module provides functions to print a welcome message, display a
shop menu, purchase items, and generate random monsters.

Functions:
    print_welcome(name: str, width: int) -> None
    print_shop_menu(item1Name: str, item1Price: float, item2Name: str, item2Price: float) -> None
    purchase_item(item_price: int, starting_money: int, qty: int = 1) -> tuple
    new_random_monster() -> dict

Typical usage:
    import gamefunctions
    gamefunctions.print_welcome("Braelyn", 40)
"""

import random

def purchase_item(item_price, starting_money, qty=1):
    """
    Calculate how many items can be purchased and money left.

    Args:
        item_price (int): Price of a single item.
        starting_money (int): Money available to spend.
        qty (int, optional): Desired quantity to purchase. Defaults to 1.

    Returns:
        tuple: (number of items purchased, money left)

    Example:
        >>> purchase_item(5, 20, 3)
        (3, 5)
    """
    can_buy = min(qty, starting_money // item_price)
    return can_buy, starting_money - can_buy * item_price


def new_random_monster():
    """
    Generate a random Shrek-themed monster with randomized stats.

    Returns:
        dict: A dictionary containing monster details:
            'name' (str), 'description' (str),
            'health' (int), 'power' (int), 'money' (int)
    """
    monsters = [
        {'name':'Lord Farquaad','desc':'A tiny tyrant with big ambitions.','h':(10,15),'p':(3,7),'m':(20,40)},
        {'name':'Donkey','desc':'A talkative donkey ready to talk your ear off.','h':(5,12),'p':(1,4),'m':(10,25)},
        {'name':'Dragon','desc':'A fiery dragon that loves treasure.','h':(15,25),'p':(5,10),'m':(30,60)},
        {'name':'Gingerbread Man','desc':'A smart cookie with a big attitude.','h':(3,8),'p':(1,3),'m':(5,15)},
        {'name':'Puss in Boots','desc':'A charming cat with sharp claws.','h':(8,14),'p':(2,6),'m':(15,35)},
    ]
    m = random.choice(monsters)
    return {
        'name': m['name'],
        'description': m['desc'],
        'health': random.randint(*m['h']),
        'power': random.randint(*m['p']),
        'money': random.randint(*m['m'])
    }


def print_welcome(name, width):
    """
    Print a welcome message centered within a given width.

    Args:
        name (str): The player's name.
        width (int): The total width to center the message.

    Returns:
        None

    Example:
        >>> print_welcome("Braelyn", 40)
    """
    print(f"Hello, {name}!".center(width))


def print_shop_menu(item1Name, item1Price, item2Name, item2Price):
    """
    Print a shop menu with two items and their prices.

    Args:
        item1Name (str): Name of the first item.
        item1Price (float): Price of the first item.
        item2Name (str): Name of the second item.
        item2Price (float): Price of the second item.

    Returns:
        None

    Example:
        >>> print_shop_menu("Potion", 5.0, "Sword", 10.0)
    """
    max_name_length = max(len(item1Name), len(item2Name))
    name_field = max(max_name_length, 12)  # minimum width for names
    price_field = 8  # fixed width for prices
    total_width = name_field + price_field + 4  # 4 for "| " and " |"
    border = "/" + "-" * (total_width - 2) + "\\"

    print(border)
    print(f"| {item1Name:<{name_field}}${item1Price:>{price_field}.2f} |")
    print(f"| {item2Name:<{name_field}}${item2Price:>{price_field}.2f} |")
    print("\\" + "-" * (total_width - 2) + "/")

def validate_input(prompt, valid_options):
    """
    Prompt the user until they enter a valid option from valid_options.
    Returns the validated input as a string.
    """
    while True:
        choice = input(prompt)
        if choice in valid_options:
            return choice
        else:
            print("Invalid input. Please try again.")

def sleep(character):
    """
    Restore HP for 5 gold if the character has enough.
    """
    if character['gold'] >= 5:
        character['hp'] += 10
        character['gold'] -= 5
        print(f"You slept like sleeping beauty and restored 10 HP. Current HP: {character['hp']}, Gold: {character['gold']}")
    else:
        print("Not enough gold to sleep")

def start_fight(character):
    """
    Handles a fight with a random Shrek-themed monster.
    Returns updated character stats.
    """
    monster = new_random_monster()
    print(f"\nA wild {monster['name']} appears!")
    print(f"Description: {monster['description']}")
    print(f"Health: {monster['health']}, Power: {monster['power']}, Gold Reward: {monster['money']}")

    while character['hp'] > 0 and monster['health'] > 0:
        print(f"\nYour HP: {character['hp']}, {monster['name']} HP: {monster['health']}")
        action = validate_input("1) Attack\n2) Run\n", ['1','2'])
        if action == '1':
            dmg_to_monster = random.randint(5, 10)
            dmg_to_character = random.randint(1, monster['power'])
            monster['health'] -= dmg_to_monster
            character['hp'] -= dmg_to_character
            print(f"You hit the {monster['name']} for {dmg_to_monster} damage!")
            print(f"The {monster['name']} hits you for {dmg_to_character} damage!")
        elif action == '2':
            print("You ran away!")
            break

    if character['hp'] <= 0:
        print("You passed out...")
    elif monster['health'] <= 0:
        gold_earned = monster['money']
        character['gold'] += gold_earned
        print(f"You defeated the {monster['name']} and earned {gold_earned} gold!")

    return character


# Test all functions when this file is run directly
def test_functions():
    """Test all functions in the module."""
    print_welcome("Braelyn", 50)
    print_shop_menu("Potion", 5.0, "Sword", 10.0)
    print(purchase_item(5, 20, 3))
    print(new_random_monster())


if __name__ == "__main__":
    test_functions()
