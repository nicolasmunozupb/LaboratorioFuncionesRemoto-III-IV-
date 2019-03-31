def perfect_number(a):
    x=0
    for i in range(1,a):
        if(a%i==0):
            x+=i
    if (x==a):
        print("It is a perfect number")
    else:
        print("It is not a perfet number")
    if x<=(a-3) and x>=(a+3):
        print("it is nt an almost perfect number")
    else:
        Print("it is an almost perfect number")

a=int(input("Type a number: "))
perfect_number(a)
