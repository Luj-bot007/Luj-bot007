a=input("Enter your name:")
b=int(input("Enter your age:"))
print("Your name is:",a)
if b>=18:

    print("You are eligible for driving.")
    c=input("Do you want to give a driving test:(yes or no):")
    if (c=="yes"):
        d=int(input ("4 wheeler or 2 wheeler(4 or 2):"))
        if d==4:
            print("Go to right.")
        elif d==2:
             print("Go to left.")
        else:
             print("Not available.")
    elif(c=="no"):
        print("Alright.")

else:
    print("You are not eligible for driving.")
print("Thank you!!")
