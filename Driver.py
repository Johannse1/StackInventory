# Evan Johanns
# stack inventory menu

from Stack import Stack


total_inventory = 0
total_profit = 0

My_Inventory = Stack()

menu_choice = int(input(""" Please type the # of the action you want to perform.
1. Add to inv.
2. Remove from inv.
3. Check profit
4. check inv.
5. Exit
>> """))

while menu_choice < 1 or menu_choice > 5:
    print(menu_choice)
    if menu_choice == 1:
        data = 0
        while data <= 1:
            Stack.push(data)

            # this is where i am stuck, after runnung this code and entering '1', the code exits instead of going into the next loop





