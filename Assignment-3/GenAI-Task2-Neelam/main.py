def factorial(n):
    # handle negative numbers
    if n < 0:
        print("Error: Factorial is not defined for negative numbers.")
        return None

    # edge cases
    if n == 0 or n == 1:
        return 1

    # recursive case
    return n * factorial(n - 1)


# test 
# factorial(5) returns 120
print(f"Factorial of 5 is: {factorial(5)}")

# factorial(0) returns 1
print(f"Factorial of 0 is: {factorial(0)}")

# factorial(-3) returns Error
print(f"Factorial of -3 is: {factorial(-3)}")