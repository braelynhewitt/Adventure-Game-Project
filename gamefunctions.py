# Braelyn Hewitt-Holbein
# Updated Game Functions - Shrek Adventure Game
# 3-5-26

import random

# Shop items with Shrek/fairy tale theme
shop_items = [
    {"name": "Happily Ever After Potion", "type": "consumable", "healAmount": 20, "price": 10},
    {"name": "Pitchforks", "type": "weapon", "maxDurability": 10, "currentDurability": 10, "equipped": False, "damage": 5, "price": 10},
    {"name": "Rumplestiltskin Magic Contract", "type": "special", "note": "Defeat a monster instantly", "uses": 1, "price": 10}
]

# Monsters
monsters = [
    {'name':'Lord Farquaad','desc':'A tiny tyrant with big ambitions.','h':(10,15),'p':(3,7),'m':(20,40)},
    {'name':'Prince Charming','desc':'Handsome charming devil.','h':(5,12),'p':(1,4),'m':(10,25)},
    {'name':'Dragon','desc':'A fiery dragon that loves towers and romance.','h':(15,25),'p':(5,10),'m':(30,60)},
    {'name':'Fairy Godmother','desc':'Evil fairy that can make all your dreams come true.','h':(3,8),'p':(1,3),'m':(5,15)},
    {'name':'Puss in Boots','desc':'A cute decieving cat with sharp claws.','h':(8,14),'p':(2,6),'m':(15,35)}
]

def print_welcome(name, width):
    print(f"Hello, {name}!".center(width))
    print("Welcome to the Shrek Adventure Game!".center(width))
    print("-"*width)

def validate_input(prompt, valid_options):
    while True:
        choice = input(prompt)
        if choice in valid_options:
            return choice
        print("Invalid input. Please try again.")

def sleep(state):
    if state["player_gold"] >= 5:
        state["player_hp"] += 10
        state["player_gold"] -= 5
        print(f"You slept like Sleeping Beauty and restored 10 HP! Current HP: {state['player_hp']}, Gold: {state['player_gold']}")
    else:
        print("Not enough gold to sleep!")

def new_random_monster():
    m = random.choice(monsters)
    return {
        'name': m['name'],
        'description': m['desc'],
        'health': random.randint(*m['h']),
        'power': random.randint(*m['p']),
        'money': random.randint(*m['m'])
    }

def start_fight(state):
    monster = new_random_monster()
    print(f"\nlook! {monster['name']} appears! {monster['description']}")
    while monster['health'] > 0 and state['player_hp'] > 0:
        print(f"\nYour HP: {state['player_hp']}, {monster['name']} HP: {monster['health']}")
        action = validate_input("1) Attack\n2) Use Special Item\n3) Run\n", ['1','2','3'])

        if action == '1':
            print("\n--- YOUR TURN ---")

            damage = random.randint(1, 5)

            weapon = None
            for item in state['player_inventory']:
                if item['type'] == 'weapon' and item.get('equipped', False):
                    weapon = item
                    damage += item['damage']
                    item['currentDurability'] -= 1

                    print(f"You attack with {item['name']}!")

                    if item['currentDurability'] <= 0:
                        print(f"Your {item['name']} broke!")
                        state['player_inventory'].remove(item)
                    break

            monster['health'] -= damage
            print(f"You dealt {damage} damage to {monster['name']}!")

            if monster['health'] <= 0:
                print(f"{monster['name']} has been defeated!")
                break

            print("\n--- MONSTER TURN ---")
            dmg_taken = random.randint(1, monster['power'])
            state['player_hp'] -= dmg_taken
            print(f"{monster['name']} hits you for {dmg_taken} damage!")

            print(f"HP -> You: {state['player_hp']} | Monster: {monster['health']}")

        elif action == '2':
            special_used = False
            for item in state['player_inventory']:
                if item['type']=='special' and item['uses']>0:
                    print(f"You used {item['name']} to defeat {monster['name']} instantly!")
                    monster['health'] = 0
                    item['uses'] -= 1
                    if item['uses']==0:
                        state['player_inventory'].remove(item)
                    special_used = True
                    break
            if not special_used:
                print("No special items available!")

        elif action == '3':
            print("You ran away safely!")
            return state

    if state['player_hp'] <= 0:
        print("You passed out... Game over!")
    else:
        print(f"You defeated {monster['name']} and earned {monster['money']} gold!")
        state['player_gold'] += monster['money']

    return state

def equip_item(state, type_filter='weapon'):
    filtered = [item for item in state['player_inventory'] if item['type']==type_filter]
    if not filtered:
        print(f"No {type_filter}s to equip.")
        return
    print("Available items to equip:")
    for i, item in enumerate(filtered, start=1):
        status = "(Equipped)" if item.get('equipped', False) else ""
        print(f"{i}) {item['name']} {status}")
    choice = input("Enter number to equip, or '-' to cancel: ")
    if choice.isdigit() and 1 <= int(choice) <= len(filtered):
        for item in state['player_inventory']:
            if item['type']==type_filter:
                item['equipped'] = False
        filtered[int(choice)-1]['equipped'] = True
        print(f"{filtered[int(choice)-1]['name']} is now equipped!")