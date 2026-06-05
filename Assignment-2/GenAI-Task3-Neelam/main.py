# user menu
orders = []

while True:

    print("1 - Add Order")
    print("2 - Show Orders")
    print("q - Quit")

    choice = input("Enter choice: ")

    if choice == "1":
        amount = input("Enter order amount: ")
        if amount.isdigit():
            amount = int(amount)
            orders.append(amount)

            print("Order Added")

        else:
            print("Invalid amount")

    elif choice == "2":

        if len(orders) == 0:
            print("No orders available")
            continue

        total = 0

        print("\nOrder  tDiscount  Final")

        for order_amount in orders:

            if order_amount >= 2000:
                discount = order_amount * 15 / 100

            elif order_amount >= 1500:
                discount = order_amount * 10 / 100

            elif order_amount >= 1000:
                discount = order_amount * 7 / 100

            else:
                discount = 0

            final_amount = order_amount - discount

            print(order_amount, "  ", discount, "   ", final_amount)

            total = total + final_amount

        print("Total:", total)

    elif choice == "q":
        print("Thank You!....Program Ended")
        break

    else:
        print("Invalid Choice")
        continue