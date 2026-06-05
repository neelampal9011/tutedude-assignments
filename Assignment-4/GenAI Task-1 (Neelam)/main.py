sales = [1200, 450, 980, 1500, 3000]
f = open("sales_data.txt", "w")
for sale in sales:
    f.write(str(sale) + "\n")
f.close()

f = open("sales_data.txt", "r")
content = f.read()
f.close()

print(content)
print(", ".join(content.splitlines()))