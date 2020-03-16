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
    r3turn = ""
    for i in range(n+1):
        r3turn = r3turn+"{:8}".format(NcR(n,i))
    return r3turn

def Pascals(n):
    for i in range(n+1):
        fstr = '{:'+str(4*(n-i))+'}'
        if i < n:
            print((fstr+'{}').format('', binomial(i)))
        else:
            print(binomial(i))


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
    Pascals(numP)


if __name__ == '__main__':
    main()