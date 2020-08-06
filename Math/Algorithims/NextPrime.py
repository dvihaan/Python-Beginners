import math

def isPrime(x):
    isit = False
    for p in range(2,int(math.sqrt(x))+1):
        print()
        if x%p == 0:
            return True

    return isit


print(isPrime(3))