#odd even
a=int(input("Enter a number :"))
if a % 2==0:
    print(a,"is even")
    for a in range  (1,10):
        if a % 2 ==0:
         print("other even numbers upto 10 are",a)
        else :
            print("__")
else:
    print(a,"is odd")
    for a in range (1,10):
        if a %2 ==0:
           print("__")
        else:
           print("other odd number upto 10 are",a)