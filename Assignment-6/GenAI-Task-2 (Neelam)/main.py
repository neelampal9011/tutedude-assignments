prices = [120, 350, 'abc', 500, -200, 800]

total = 0
for item in prices:
    try:
        if type(item) == str:
            raise TypeError("string not allowed")
        price = int(item)
        if price < 0:
            raise ValueError("negative price not allowed")
    except TypeError:
        print(f"skipping invalid item: {item}")
        continue
    except ValueError:
        print(f"skipping invalid item: {item}")
        continue
    else:
        total += price

print("running total:", total)