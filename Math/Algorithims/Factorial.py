
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
    for i in range(n+1):
        print(NcR(n,i),end = '\t')

def allFactorials(n):
    for i in range(n+1):
        print('{:>166}'.format(factorialRecursive(i)))

def main():
    
    num1 = 5
    '''
    num2 = 2

    factorial = NcR(num1,num2)
    print(factorial)
    '''

    binomial(num1)   

if __name__ == '__main__':
    main()