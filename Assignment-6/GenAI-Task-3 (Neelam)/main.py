def check_age(age):
    if age < 1 or age > 120:
        raise ValueError("Age must be between 1 and 120")

try:
    age = int(input("Enter your age: "))
    check_age(age)

except ValueError:
    print("Error: Age must be between 1 and 120")

else:
    print("valid age")

finally:
    print("age check completed")