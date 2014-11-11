import math
def isprime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    prime = True
    for x in range (2,n):
        
        if n%x == 0:
            prime = False
    return prime

    
def primesto(n):
    for x in range (1,n+1):
        if isprime(x):
            print x



num = input('Enter a number to get Primes: ')
primesto(num)

# Looks good to me Justin
