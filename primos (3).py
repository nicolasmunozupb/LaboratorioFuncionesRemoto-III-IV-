def is_prime(a):
    count=0
    for i in range(1,a+1):
        if a % i == 0:
            count=count+1
    if count == 2:
        a=a**0
        return a
    else:
        a=a*0
        return a
#---------------------------------
prc=0
while True:
    prc=prc+1
    try:
        x=int(input("Type a Number: "))
        if x<=0:
            print("The number is zero or less than zero, so GG")
            break
        primo=is_prime(x)
        if primo==0:
            print(primo)
        else:
            print(primo)
    except Exception:
        print("-1")

counter=0
for i in range(1,prc+1):
    if prc% i==0:
        counter=counter+1
if counter==2:
    print("The number of times calculated is prime and is",prc)
else:
    print("The number of times calculated is not prime and is",prc)
