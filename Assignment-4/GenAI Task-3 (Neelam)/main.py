with open("sales_data.txt", "a") as f:
    new_sales = [5000, 2500, 1700]

    for sale in new_sales:
        f.write(str(sale) + "\n")

with open("sales_data.txt", "r") as f:
    updated = f.readlines()
    print(updated)

updated_list = [int(sale.strip()) for sale in updated if sale.strip()]

print(updated_list)
print(f'total no of lines in the file: {len(updated_list)}')

    