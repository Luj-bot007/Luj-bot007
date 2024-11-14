a=int(input("Enter any number of day(1 to 7):"))
match a:
    case 1:
        print("Today is Sunday.")
    case 2:
        print("Today is Monday.")
    case 3:
        print("Today is Tuesday.")
    case 4:
        print("Today is Wednesday.")
    case 5:
        print("Today is thrusday.")
    case 6:
        print("Today is Friday.")
    case 7:
        print("Today is Saturday.")
    case _:
        print("Invalid.")
if (a==1):
    print("Today you have work at 5pm.")
elif (a==2):
    i=0
    for i in range (3):

        if i==0:
             print ("You have  essential class .")
        elif i==1:
            print ("You have communication class.")
        elif i==2:
            print("You have lab.")
elif (a==3):
    i=0
    for i in range (3):

        if i==0:
             print ("You have  AS class .")
        elif i==1:
            print ("You have math class.")
        elif i==2:
            print("You have Java class.")
elif (a==4):
    i=0
    for i in range (2):

        if i==0:
             print ("You have  db class .")

        elif i==1:
            print("You have java lab.")

elif (a==5):
    i=0
    for i in range (2):
        if i==0:
             print ("You have  math class .")
        elif i==1:
            print("You have lab.")
if (a==6):
    print("Today you have work at 5pm.")
if (a==7):
    print("Today you have work at 5pm.")