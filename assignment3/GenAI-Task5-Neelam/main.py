prices = [100, 250, 400, 1200, 50, 2000, 850]

greater_than_500 = list(filter(lambda price: price > 500, prices))
less_or_equal_500 = list(filter(lambda price: price <= 500, prices))

print("prices > 500:", greater_than_500)
print("prices <= 500:", less_or_equal_500)