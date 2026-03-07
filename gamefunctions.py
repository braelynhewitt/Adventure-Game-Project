# Braelyn Hewitt-Holbein
# Updated Game functions
# 3-1-26

import random

# buy items
def purchase_item(item_price, starting_money, qty=1):
    """Return how many items you can buy and money left"""
    can_buy = min(qty, starting_money // item_price)
    return can_buy, starting_money - can_buy * item_price

# random monster
def new_random_monster():
    """Create a random monster with stats"""
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

# welcome message
def print_welcome(name, width):
    """Print a welcome message centered in width"""
    print(f"Hello, {name}!".center(width))

# shop menu with dynamic width
def print_shop_menu(item1Name, item1Price, item2Name, item2Price):
    """Print a shop menu with two items and prices"""
    # find the longest item name length
    max_name_length = max(len(item1Name), len(item2Name))
    name_field = max(max_name_length, 12)  # at least 12
    price_field = 8  # keep price width fixed
    total_width = name_field + price_field + 4  # 4 for "| " and " |"  
    border = "/" + "-" * (total_width - 2) + "\\"

    print(border)
    print(f"| {item1Name:<{name_field}}${item1Price:>{price_field}.2f} |")
    print(f"| {item2Name:<{name_field}}${item2Price:>{price_field}.2f} |")
    print("\\" + "-" * (total_width - 2) + "/")

