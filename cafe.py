cafe_name = "SHRUTIKA's CAFE"
BOLD = "\033[1m"
END = "\033[0m"

print(f"                                      {BOLD}WELCOME TO {cafe_name}{END}\n")

print(f"                                               {BOLD}MENU{END}\n")

# ESPRESSO MENU
print(f"{BOLD}ESPRESSO{END}\n")

Espresso_menu = {
    "Espresso": 2.00,
    "Macchiato": 2.50,
    "Latte": 2.50,
    "Breve": 2.50,
    "Mocha": 3.00,
    "Cappuccino": 3.00,
    "Americano": 2.00
}

for item, price in Espresso_menu.items():
    print(f"{item:<25} ${price}")

print()

# HOT MENU
print(f"{BOLD}HOT{END}\n")

Hot_menu = {
    "Daily Dark Roast": 2.75,
    "Pour Over": 3.25,
    "Hot Chocolate": 3.00,
    "Steamer": 3.00,
    "Cafe Au Lait": 4.00
}

for item, price in Hot_menu.items():
    print(f"{item:<25} ${price}")

print()

# QUICK BITES
print(f"{BOLD}QUICK BITES{END}\n")

Quick_bites_menu = {
    "Bagel": 2.00,
    "Muffin": 2.20,
    "Breakfast Sandwich": 4.75,
    "Croissant": 1.75,
    "Scones": 2.25
}

for item, price in Quick_bites_menu.items():
    print(f"{item:<25} ${price}")

print("\nWhat would you order?\n")

# MERGE ALL MENUS
merged_menu = Espresso_menu | Hot_menu | Quick_bites_menu

order_menu_list = []

while True:
    order_name = input("Enter item name (or type 'done' to finish): ")

    if order_name.lower() == "done":
        break

    if order_name not in merged_menu:
        print("Item not found in menu. Please try again.")
        continue

    try:
        quantity = int(input(f"Enter quantity for {order_name}: "))
        order_menu_list.append({"item": order_name, "quantity": quantity})
    except ValueError:
        print("Invalid input for quantity. Please enter a number.")

print()
print(f"{BOLD}*************** RECEIPT ***************{END}\n")
print(f"{BOLD}ITEMS x QUANTITY x PRICE{END}\n")

total_quantity = 0
total_price = 0

for order in order_menu_list:
    item = order["item"]
    quantity = order["quantity"]
    price = merged_menu[item]

    item_total = price * quantity

    total_quantity += quantity
    total_price += item_total

    print(f"{item:<20} x {quantity:<3} x ${price} = ${item_total:.2f}")

print()
print(f"TOTAL ITEMS: {total_quantity}")
print(f"TOTAL PRICE: ${total_price:.2f}")


