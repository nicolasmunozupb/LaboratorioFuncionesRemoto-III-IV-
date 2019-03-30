def perfect_number(a):
    x=0
    for i in range(1,a):
        if(a%i==0):
            x+=i
    if (x==a):
        print("It is a perfect number")
    else:
        print("It is not a perfet number")

a=int(input("Type a number: "))
perfect_number(a)
