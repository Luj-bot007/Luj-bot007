def number(a):
    if a % 2==0:
        return "even"
    else:
        return "odd"

a=float(input("Enter the number:"))

result=number(a)
print(f"The number is {result}")
