# multiple order processing

order = [1200, 2500, 800, 1750, 3000]

total_revenue = 0
count_discount_order = 0
print("order amount    discount   final amount")
for order_amount in order:
    if order_amount >= 2000:
        discount = order_amount * 15/100

    elif order_amount >= 1500:
        discount = order_amount * 10/100

    elif order_amount >= 1000:
        discount = order_amount * 7/100

    else:
        discount = 0

    final_amount = order_amount - discount

    
    print(order_amount,'    ',discount,'    ',final_amount)
    total_revenue += final_amount

    if discount > 0:
        count_discount_order += 1

print('total_revenue:', total_revenue)
print("order with discount:", count_discount_order)