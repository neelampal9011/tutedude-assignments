# GST lambda
gst = lambda price: price + (18/100*price)

prices = [100, 250, 400, 1200, 50]

prices_with_gst = list(map(gst, prices))

print("original prices:", prices)
print("prices after GST:", prices_with_gst)