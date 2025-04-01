def print_menu():
    menu = {
        '1' : ("Classic Burger", 5),
        '2' : ("Regular Burger", 3),
        '3' : ("Chicken Burger", 4),
        '4' : ("Chicken Chees Melt", 2),
        '5' : ("Mazarella Burger", 6),
        '7' : ("Double Chicken Burger", 7),
        '8' : ("Beef Burger", 3),
        '9' : ("Double Beef Burger", 7)
    }
    print("--------------------------------Menu List--------------------------------")
    print(f"{'S.No':<5}| {'Name':^25}| {'Price'}")
    print("-------------------------------------------------------------------------")

    for keys, values in menu.items():
        print(f"{keys + '.':<5}| {values[0]:^25}| {values[1]}$")
    print("-------------------------------------------------------------------------")
    return menu

def get_order(menu):
    item = input("Enter the number of the item you want to order ('#' to 'quit'): ")
    orders = []
    while(item!='#'):
        if item in menu:
            quantity = int(input("How much quantity you want: "))
            orders.append((menu[item][0], menu[item][1], quantity))
        else:
            print('Invalid selection, try again.')
        item = input("Enter the number of the item you want to order ('#' to 'quit'): ")
    return orders
def calculate_bill(order):
    bill_amount = 0
    for (name, price, quantity) in order:
        bill_amount += price * quantity
    total_amount = bill_amount
    print('-' * 75)
    student_discount = input("Are you a student? ('#' for 'yes' or '*' for 'no'): ")
    discount = 0
    if(student_discount == '#'):
        discount = (bill_amount/100) * 20
        total_amount -= discount
    delivery = input("Do you want delivery? ('#' for 'yes' or '*' for 'no'): ")
    delivery_charge = 0
    if(delivery == '#'):
        delivery_charge = (bill_amount/100) * 5
        total_amount += delivery_charge

    while True:
        tip_amount = input("Do you want to give tip? (0 for no tip): $")
        if tip_amount.isdigit():
            total_amount += int(tip_amount)
            break
        else:
            print("Invalid input, try again.")
    return (discount, delivery_charge, tip_amount, bill_amount, total_amount)

def print_bill(order, bill):
    print("\n********************************Final Bill**********************************")
    print(f"{'S.NO':3}| {'Name':^25} | {'Price':^10} | {'Quantity':^10} | {'Total Price'}")
    print('-' * 75)
    sno = 1
    for (name, price, quantity) in order:
        print(f"{sno:3}.| {name:^25} | {str(price)+'$':<10} | {quantity:^10} | {price*quantity}$")
        sno += 1
    print('-' * 75)
    print(f"Before Discount Total Bill{str(bill[3])+'$':>37}")
    print(f'Student Discount 20%{"-"+str(bill[0])+"$":>43}')
    print(f'Delivery Charge 5%{"+"+str(bill[1])+"$":>45}')
    print(f'Tip{"+"+str(bill[2])+"$":>60}')
    print('-' * 75)
    print(f'Total Bill{str(bill[4])+"$":>53}')
    print("\nThank you and come again>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

def main():
    menu = print_menu()
    order = get_order(menu)
    if order:
        bill = calculate_bill(order)
        print_bill(order, bill)
    else:
        print('-' * 75)
        print("YOU HAVE NO ORDER!\nTHANK YOU🫂")

if __name__ == "__main__":
    main()
