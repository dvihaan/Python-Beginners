import math
import PrimeFactorTools

def PerfectNumbers(c):
    r = 0
    pns = []
    for i in range(c):
        r = PrimeFactorTools.nextPrime(r)
        pns.append(r)
    pfl = []
    for pn in pns:

        m = (2**pn-1)
        print(f'm={m}')
        if PrimeFactorTools.isPrime(m) == True:
            prf = 2**(pn-1)*m
            pfl.append((pn, prf))
        else:
             print(f'Prime No . {pn} doesn\'t yield a perfect number')

        '''
        prf = 2**(pn-1)*(2**pn-1)
        if PrimeFactorTools.factorSum(prf) == prf:
            pfl.append((pn, prf))
        else:
            print(f'Prime No . {pn} doesn\'t yield a perfect number')
        '''
    return pfl

print(PerfectNumbers(17))
