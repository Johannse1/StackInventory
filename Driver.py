# Evan Johanns
# stack inventory menu

from Stack import Stack


total_inventory = 0
total_profit = 0
total_value_sold = 0


Inventory = Stack()
Price = Stack()


choice = 0
while choice != 5:
    print("""
    1. Add to inv.
    2. Sell inv.
    3. Check inv.
    4. Check profit
    5. Exit""")
    choice = int(input(">>"))
    if choice == 1: # adding to inventory
        qty = int(input("How much is being added?:"))
        price = int(input("How much does it cost?:"))
        Inventory.push(qty) # Inventory stack
        Price.push(price) #
        print("Inventory added. \n\n")

        total_inventory += qty # running total

    elif choice == 2:
        qty_needed = int(input("How mauch are you looking to sell?"))
        if qty_needed > Inventory:
            print("Not enough inv to fulfill order, try again. \n\n")
            continue
        else:
            total_popped = 0
            total_sale = 0.0
            # next lines keep track of where you are
            qty_popped = Inventory.pop()
            total_inventory -= qty_popped
            price = Inventory.pop()
            total_sale += (qty_popped * price)
            total_popped += qty_popped
            # keep poppong until we hve enough
            while total_popped < qty_needed:
                qty_popped = Inventory.pop()
                total_inventory -= qty_popped
                price = Inventory.pop()
                total_sale += (qty_popped * price)
                total_popped += qty_popped
                #incase we popped too many
                if total_popped > qty_needed:
                    overage = total_popped - qty_needed
                    Inventory.push(overage)
                    Price.push(price)
                    total_inventory += overage
                    total_sale -= (total_sale * .1)
                    print(f"Order comlpete for {qty_needed}\n")

    if choice == 3:
        print(f"Total inventory: {total_inventory}\n")

    if choice == 4:
        print(f"Total profit: ${total_profit}\n")










