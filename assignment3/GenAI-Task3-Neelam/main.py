# GST lambda (18%)
gst = lambda price: price + (0.18*price)

print(gst(100))  # 118.0

# extra: GST + 10% discount
gst_discount = lambda price: (price + (0.18*price)) * 0.90

print(gst_discount(100))  # 106