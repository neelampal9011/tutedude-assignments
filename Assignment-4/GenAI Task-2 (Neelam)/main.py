with open("sales_data.txt", "r") as f:
    data = f.read()
    print(data)

with open("sales_data.txt", "r") as f:
    line = f.readline()
    print(line)
    

with open("sales_data.txt", "r") as f:
    lines = f.readlines()
    print(lines)

clean_list = [int(line.strip()) for line in lines]   
print(clean_list)