# Braelyn Hewitt-Holbein
# Adventure Game Main Script - Shrek Adventure
# 3-5-26

import gamefunctions

def main():
    name = input("Enter your name, adventurer: ")
    gamefunctions.print_welcome(name, 50)

    # Initialize state
    state = {
        "player_name": name,
        "player_hp": 30,
        "player_gold": 75,
        "player_inventory": []
    }

    while True:
        print(f"\nHP: {state['player_hp']}, Gold: {state['player_gold']}")
        choice = gamefunctions.validate_input(
            "1) Fight Monster\n2) Sleep (5 gold)\n3) Visit Shop\n4) Equip Weapon\n5) Quit\n",
            ['1','2','3','4','5']
        )

        if choice=='1':
            state = gamefunctions.start_fight(state)
        elif choice=='2':
            gamefunctions.sleep(state)
        elif choice=='3':
            print("\nWelcome to the Shop!")
            for idx, item in enumerate(gamefunctions.shop_items, start=1):
                if item['type']=='consumable':
                    extra = f"(Heals {item['healAmount']} HP)"
                elif item['type']=='weapon':
                    extra = f"(Damage: {item['damage']}, Durability: {item['currentDurability']})"
                else:
                    extra = f"({item['note']})"
                print(f"{idx}) {item['name']} {extra} - Price: {item['price']} gold")
            choice_shop = input("Enter number to buy or '-' to cancel: ")
            if choice_shop.isdigit() and 1 <= int(choice_shop) <= len(gamefunctions.shop_items):
                item = gamefunctions.shop_items[int(choice_shop)-1].copy()
                if state['player_gold'] >= item['price']:
                    state['player_inventory'].append(item)
                    state['player_gold'] -= item['price']
                    print(f"You purchased {item['name']}!")
                else:
                    print("Not enough gold!")
        elif choice=='4':
            gamefunctions.equip_item(state)
        elif choice=='5':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()