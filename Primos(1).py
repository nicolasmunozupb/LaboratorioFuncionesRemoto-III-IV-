def is_prime(a):
    cont=0
    for i in range(1,a+1):
        if a%i==0:
            cont=cont+1
        
    if cont>2:
        print("Is not a prime number")
    else:
        print("Is a prime number")
#------------------------------------
        
a=int(input("Type a number"))
is_prime(a)
