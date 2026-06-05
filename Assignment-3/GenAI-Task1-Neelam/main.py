def apply_discount(price, discount_percent=5):  

    if discount_percent > 60:        # Ensure discount does not exceed 60%
        discount_percent = 60

    discounted_price = price - (price * discount_percent / 100)
    return discounted_price


# test 
# apply_discount(1000, 10) returns 900.0
print(f"Discounted price of 1000 with 10% discount is : {apply_discount(1000, 10)}")

# apply_discount(500) returns 475.0
print(f"Discounted price of 500 with 5% discount is : {apply_discount(500)}")

# 70% is greater than 60% so discount will be 60%
print(f"Discounted price of 1000 with 70% discount is : {apply_discount(1000, 70)}")