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
    Generate a random monster with randomized stats.

    Returns:
        dict: A dictionary containing monster details:
            'name' (str), 'description' (str),
            'health' (int), 'power' (int), 'money' (int)

    Example:
        >>> new_random_monster()
        {'name': 'Goblin', 'description': 'A big scared goblin.', 'health': 10,
         'power': 3, 'money': 25}
    """
    monsters = [
        {'name':'Goblin','desc':'A big scared goblin.','h':(5,15),'p':(1,5),'m':(10,50)},
        {'name':'Vulture','desc':'A comical angry vulture.','h':(1,3),'p':(0,2),'m':(5,25)},
        {'name':'Zombie Bear','desc':'A hungry half dead bear.','h':(10,20),'p':(5,10),'m':(20,100)}
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


# Test all functions when this file is run directly
def test_functions():
    """Test all functions in the module."""
    print_welcome("Braelyn", 50)
    print_shop_menu("Potion", 5.0, "Sword", 10.0)
    print(purchase_item(5, 20, 3))
    print(new_random_monster())


if __name__ == "__main__":
    test_functions()
