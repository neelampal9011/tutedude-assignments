def process_prices(prices):
    # apply 10% discount
    discounted_prices = list(map(lambda price: price * 90/100, prices))

    # keep only prices above 300
    filtered_prices = list(filter(lambda price: price > 300, discounted_prices))

    return discounted_prices, filtered_prices


# test
discounted_prices, filtered_prices = process_prices([100, 500, 900, 50, 750])

print("discounted prices:", discounted_prices)
print("filtered prices:", filtered_prices)