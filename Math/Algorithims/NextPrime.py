import math

def isPrime(x):
    if x == 1:
        return False
    isit = True
    for p in range(2,math.ceil(math.sqrt(x))+1):
        print(p)
        if x%p == 0 and x != p:
            isit = False
            break

    return isit


print(isPrime(1))