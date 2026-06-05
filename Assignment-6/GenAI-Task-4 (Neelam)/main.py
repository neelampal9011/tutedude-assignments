try:
    filename = input("Enter file name: ")
    file = open(filename, "r")
    lines = file.readlines()

except FileNotFoundError:
    print("Error: File not found")

except PermissionError:
    print("Error: Permission denied")

else:
    for line in lines[:3]:
        print(line)
    print("first 3 lines printed successfully")
finally:
    print("File operation attempted.")