try:
    numerator = float(input("Enter numerator: "))
    denominator = float(input("Enter denominator: "))

    result = numerator / denominator

except ValueError:
    print("Error: please enter valid numbers only")

except ZeroDivisionError:
    print("Error: denominator cannot be zero")

else:
    print("answer is: ", result)

finally:
    print("Operation Complete")