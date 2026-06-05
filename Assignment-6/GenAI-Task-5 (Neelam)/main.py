cart = []
total = 0

while True:
    user_input = input("Enter price (or 'q' to quit): ")
    if user_input.lower() == 'q':
        break
    try:
        price = float(user_input)

        if price < 0:
            raise ValueError("negative price not allowed")

    except ValueError:
        print("Invalid input. try again.")
        continue

    else:
        cart.append(price)
        total += price

print("total items:", len(cart))
print("your total bill is: ", total)