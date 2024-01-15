import os
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

primary_color: str = Fore.LIGHTGREEN_EX
secondary_color: str = Fore.CYAN
error_color: str = Fore.LIGHTRED_EX


class InventoryItem:
    name: str
    price: float
    count: int

    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count


inventory: list[InventoryItem] = list()
cash_balance: float = 100.0


def display_main_menu() -> int:
    os.system('cls')
    print(f'{primary_color}MENU{Style.RESET_ALL}')
    print(' 1. Sell groceries')
    print(' 2. Manage Inventory')
    print(' 3. Import data from Excel')
    print(' 4. Export data to Excel')
    print(' 5. Edit cash balance')
    print(' 6. View cash balance')
    print(' 0. Exit')

    user_choice: int = int(input(f'\n{secondary_color}Choose an option from the above: {Style.RESET_ALL}'))
    return user_choice


def display_inventory_menu() -> None:
    exit_chosen: bool = False
    while not exit_chosen:
        os.system('cls')
        print(f'{primary_color}MANAGE INVENTORY{Style.RESET_ALL}')
        print(' 1. View inventory')
        print(' 2. Add new item type to inventory')
        print(' 3. Delete item type from inventory')
        print(' 4. Edit item type in inventory')
        print(' 5. Return to Main Menu')

        user_choice: int = int(input(f'\n{secondary_color}Choose an option from the above: {Style.RESET_ALL}'))

        match user_choice:
            case 1:
                display_inventory()
                input('\nPress enter to continue...')
            case 2:
                add_new_item_type_to_inventory()
                input('\nPress enter to continue...')
            case 3:
                delete_item_type_from_inventory()
                input('\nPress enter to continue...')
            case 5:
                return


def display_inventory():
    os.system('cls')
    print(f'{primary_color}Displaying Inventory{Style.RESET_ALL}\n')
    if len(inventory) == 0:
        print('You currently have no inventory.')
    else:
        print(f'{secondary_color}Name\tCount\tCost{Style.RESET_ALL}')
        for inventory_item in inventory:
            print(f'{inventory_item.name}\t{inventory_item.count}\t{inventory_item.price}')


def add_new_item_type_to_inventory():
    os.system('cls')
    print(f'{primary_color}Adding New Item Type to Inventory{Style.RESET_ALL}\n')

    valid_name: bool = False
    name: str = ''

    while not valid_name:
        name = input(f'Enter the name of the item type (e.g. "Apple"): {primary_color}')
        print(f'{Style.RESET_ALL}', end='')

        if len(inventory) == 0:
            valid_name = True

        for inventory_item in inventory:
            if str.upper(inventory_item.name) == str.upper(name):
                print(f'{error_color}Invalid name "{name}".')
                print(f'An item with that name already exists in inventory.{Style.RESET_ALL}')
            else:
                valid_name = True

    price: float = float(input(f'Enter the price of the item: {primary_color}'))
    print(f'{Style.RESET_ALL}', end='')

    count: int = int(input(f'Enter the number of items to add to the inventory: {primary_color}'))
    print(f'{Style.RESET_ALL}', end='')

    new_inventory_item: InventoryItem = InventoryItem(name=name, price=price, count=count)
    inventory.append(new_inventory_item)


def delete_item_type_from_inventory() -> None:
    os.system('cls')
    if len(inventory) == 0:
        print(f'{error_color}You must have at least one inventory item to delete any.')
        return

    valid_name: bool = False

    while not valid_name:
        name: str = input(f'Enter the name of the item type you would like to delete: {primary_color}')
        print(f'{Style.RESET_ALL}', end='')
        for inventory_item in inventory:
            if str.upper(inventory_item.name) == str.upper(name):
                print(f'{secondary_color}Deleting {inventory_item.name} from inventory...')
                inventory.remove(inventory_item)
                valid_name = True
            else:
                print(f'{error_color}Invalid name "{name}".')
                print(f'Item not found in inventory.{Style.RESET_ALL}')


def display_cash_balance() -> None:
    os.system('cls')
    print(f'{primary_color}Displaying Cash Balance\n{Style.RESET_ALL}')
    print(f'Current Cash Balance: {secondary_color}{cash_balance}{Style.RESET_ALL}')


def edit_cash_balance() -> None:
    os.system('cls')
    global cash_balance
    print(f'{primary_color}Editing Cash Balance\n{Style.RESET_ALL}')
    print(f'Current Cash Balance: {secondary_color}{cash_balance}{Style.RESET_ALL}')
    new_cash_balance: float = float(input(f'Enter new Cash Balance: {secondary_color}'))
    cash_balance = new_cash_balance
    print(f'{Style.RESET_ALL}', end='')


def sell_groceries() -> None:
    print(f'{primary_color}Sell Groceries\n{Style.RESET_ALL}')
    print(f'Enter a comma separated list of grocery items and the quantities sold '
          f'e.g., "Apples 3, Bananas 5, Carrots 2".')
    groceries_sold: str = input()
    grocery_list: list[str] = [s.strip() for s in str.split(groceries_sold, ',')]
    groceries_sold_summary: dict[str, (int, float)] = dict()
    for grocery in grocery_list:
        grocery_name: str = str.upper(grocery.split(' ')[0])
        grocery_quantity_sold: float = float(grocery.split(' ')[1].strip())

        for inventory_item in inventory:
            if grocery_name == inventory_item.name:
                groceries_sold_summary[grocery_name] = (grocery_quantity_sold, inventory_item.price)



colorama_init()
exit_chosen: bool = False

while not exit_chosen:
    os.system('cls')
    user_choice: int = display_main_menu()

    match user_choice:
        case 2:
            display_inventory_menu()
            input('\nPress enter to continue...')
        case 5:
            edit_cash_balance()
            input('\nPress enter to continue...')
        case 6:
            display_cash_balance()
            input('\nPress enter to continue...')
        case 0:
            exit_chosen = True

