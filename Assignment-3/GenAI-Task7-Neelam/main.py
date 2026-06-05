# menu using functions
def add_price(prices_list, price):
    prices_list.append(price)
    print("price added successfully!")


def get_average_price(prices_list):
    if len(prices_list) == 0:
        return 0
    return sum(prices_list) / len(prices_list)


def get_max_price(prices_list):
    if len(prices_list) == 0:
        return None
    return max(prices_list)


# main program
prices = []

while True:
    print("............ PRICE MENU ............  ")
    print("1 -> add price")
    print("2 -> show average price")
    print("3 -> show highest price")
    print("q -> quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        price = float(input("Enter price: "))
        add_price(prices, price)

    elif choice == "2":
        avg = get_average_price(prices)
        print("average price:", avg)

    elif choice == "3":
        highest = get_max_price(prices)

        if highest is None:
            print("no prices available.")
        else:
            print("highest price:", highest)

    elif choice.lower() == "q":
        print("exiting program...")
        break

    else:
        print("Invalid choice! please try again.")
        