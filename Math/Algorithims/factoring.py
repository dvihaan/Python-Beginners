import math

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

def main():
    num = 36
    factors = allfactors(num)
    print(sorted(set(factors)))
    fancyfactors(num)

if __name__ == '__main__':
    main()