import math
from multiset import Multiset

def allfactors(n):
    factors = []
    for i in range(1,int(math.sqrt(n))+1):
        if n%i == 0:
            addedfactors = [i,int(n/i)]
            factors.extend(addedfactors)
    return factors


'''
def orderfactors(n):
    factors = []
    for i in range(1,n+1):
        if n%i == 0:
            factors.append(i)
    return factors
'''

def fancyfactors(n):
    factors = allfactors(n)
    l = len(factors)
    for i in range(0,l-1,2):
        print(f"{n} = {factors[i]} * {factors[i+1]}")

def smallestfactor(n):
    for i in range(2,int(math.sqrt(n))+1,1):
        if n%i == 0:
            return i
    return n

def primefactors(n):
    factors = []
    sf = smallestfactor(n)
    factors.append(sf)
    n = int(n/sf)
    while sf <= n:
        sf = smallestfactor(n)
        n = int(n/sf)
        factors.append(sf)
    return factors

def GCF(x,y):
    pfx = Multiset(primefactors(x))
    pfy = Multiset(primefactors(y))
    gcf = 1
    for p in pfx.intersection(pfy):
        gcf = gcf*p
    return gcf

def LCM(x,y):
    pfx = Multiset(primefactors(x))
    pfy = Multiset(primefactors(y))
    gcf = 1
    union = pfx.union(pfy)
    for p in union:
        gcf = gcf*p
    return gcf

def main():
    num = 13082761331670030
    n1 = 180
    n2 = 252
    factors = primefactors(num)
    venn = LCM(n1,n2)
    print(venn)
    #fancyfactors(num)                                              

if __name__ == '__main__':
    main()