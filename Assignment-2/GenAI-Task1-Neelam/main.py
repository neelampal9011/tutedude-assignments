# discount rule

order_amount = input("Enter the order amount: ")

if order_amount.isdigit():
    order_amount = int(order_amount)
    
    if order_amount >= 2000:
        discount = order_amount * 15/100

    elif order_amount >= 1500:
        discount = order_amount * 10/100

    elif order_amount >= 1000:
        discount = order_amount * 7/100

    else:
        discount = 0

    subtotal = order_amount - discount
    tax = subtotal * 5/100
    final_total = subtotal + tax

    print("Order amount:", order_amount)
    print("Discount:", discount)
    print("Subtotal:", subtotal)
    print("Tax:", tax)
    print("Final amount:", final_total)

else:
    print("error: please enter a numerical value for order amount")

        
