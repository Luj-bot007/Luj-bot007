def number(a):
    if a > 0:
        return "Positive"
    elif a < 0:
        return "Negative"
    else:
        return "Zero"

# Get user input
a = float(input("Enter the number: "))

# Call the function and print the result
result = number(a)
print(f"The number is {result}.")
