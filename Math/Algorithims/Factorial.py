def factorialLoop(n):
    ans = 1
    for i in range(1,n+1):
        ans = ans*i
    return ans

def factorialRecursive(n):
    if n == 0:
        return 1
    return n*factorialRecursive(n-1)

def NcR(n,r):
    return int(factorialLoop(n)/(factorialLoop(r)*factorialLoop(n-r)))

def binomial(n):
    terms = []
    for i in range(n+1):
        terms.append(NcR(n,i))
    return terms

def Pascals(n,w = 4):
    for i in range(n+1):
        sw = '{:'+str(w*(n-i))+'}'
        fw = '{:'+str(2*w)+'}'
        terms = binomial(i)
        bn = ""
        for term in terms:
            bn = bn+fw.format(term)
        if i < n:
            print((sw+'{}').format('', bn))
        else:
            print(bn)


def allFactorials(n):
    for i in range(n+1):
        print('{:>165}'.format(factorialRecursive(i)))

def main():
    '''
    numFL = 5
    print(factorialLoop(numFL))

    numFR = 5
    print(factorialRecursive(numFR))  

    numAF = 5
    allFactorials(numAF)

    numN = 5
    numR = 2
    print(NcR(numN,numR)) 

    numB = 6
    print(binomial(numB))

    '''
    numP = 10
    fillwidth = 3
    Pascals(numP,fillwidth)


if __name__ == '__main__':
    main()