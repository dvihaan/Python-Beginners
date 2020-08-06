import math

def isPrime(x):
    if x == 1:
        return False
    isit = True
    for p in range(2,math.ceil(math.sqrt(x))+1):
        if x%p == 0 and x != p:
            isit = False
            break

    return isit

def nextPrime(c):
    i = c+1
    while True:
        if isPrime(i) == True:
            return i
        i += 1

def allFactors(n):
    factorList = set()
    for i in range(1, math.ceil(math.sqrt(n))+1):
        if n%i == 0:
            factorList.add(int(n/i))
            factorList.add(i)
    return list(factorList)

def factorSum(f):
    return sum(allFactors(f)[:-1])

print(factorSum(6))