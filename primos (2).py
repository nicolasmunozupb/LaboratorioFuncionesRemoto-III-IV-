def is_prime(a):
    count=0
    for i in range(1,a+1):
        if a % i == 0:
            count=count+1
    if count==2:
        a=a**0
        return a
    else:
        a=a*0
        return a
#-------------------------------------
while True:
    try:
        x=int(input("Type a number"))
        if x<=0:
            print("The number is zero or less than zero, so GG")
            break
        prime=is_prime(x)
        if prime==0:
            print(prime)
        else:
            print(prime)
    except Exception:
        print("-1")
