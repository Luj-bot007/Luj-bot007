def day(a):
    if a==1:
        return("Sunday")
    elif a==2:
        return("Monday")
    elif a==3:
        return("Tuesday")
    elif a==4:
        return("Wednesday")
    elif a==5:
        return("Thrusday")
    elif a==6:
        return("Friday")
    else:
        return ("Saturday")

a=float(input("Enter a number "))
result = day(a)
print(f"Today is :{result}")

for a in range (1 101 ):
    print (a)