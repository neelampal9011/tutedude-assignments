# Product dictionary
prices = {
    "Mouse": 500,
    "Keyboard": 800,
    "Monitor": 7000,
    "Pendrive": 400,
    "Camera": 5000
}
discount = int(input("enter discount percentage: "))

f = open("discount_report.txt", "w")
f.write("Product | Original Price | Discounted Price\n")

total = 0
count = 0
for product, price in prices.items():
    if discount > 90:
        discount = 90
    discounted_price = price - (price * discount / 100)
    f.write(product + " | " + str(price) + " | " + str(discounted_price) + "\n")

    total += discounted_price
    count += 1

# Summary
# average = total / count
f.write("total items: " + str(count) + "\n")
f.write("average discounted price: " + str(total/count) + "\n")

f.close()

f = open("discount_report.txt", "r")
print(f.read())
f.close()