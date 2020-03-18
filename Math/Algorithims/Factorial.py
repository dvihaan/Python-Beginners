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

def power(base='x', n=1, suppress = True):
    index = ''
    if n == 0:
        if suppress == True:
            return ''
        else:
            return(base+chr(int('0x2070', 16)))
    if n ==1:
        if suppress == True:
            return(base+index)
        else:
            return(base+chr(int('0x00B9', 16)))
    digits = []
    while n > 0:
        digits.append(n%10)
        n = int(n/10)
    digits.reverse()
    superscript_digits = []
    for d in digits:
        if d ==1:
            superscript_digits.append(chr(int('0x00B'+str(10-d), 16)))
        elif d ==2 or d==3:
            superscript_digits.append(chr(int('0x00B'+str(d), 16)))
        else:
            superscript_digits.append(chr(int('0x207'+str(d), 16)))
    for s in superscript_digits:
        index = index + s
    return(base+index)


def Wholepower(n):
    ptr = binomial(n)
    answer = power('(a+b)',n,False)+" = "
    if n == 0:
        answer = answer+'1'
    for i in range(len(ptr)):
        if ptr[i] == 1:
            if n-i == 0:
                answer = answer+power('b',i,)
            elif i == 0:
                answer = answer+power('a',n-i)+" + "
        else:
            answer = answer+str(ptr[i])+power('a',n-i)+power('b',i)+" + "
    print(answer)

def binomialIdentities(n):
    for i in range(0,n+1,1):
        Wholepower(i)

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
    numP = 14
    fillwidth = 3
    Pascals(numP,fillwidth)
    print("")
    binomialIdentities(numP)
                                                                    
if __name__ == '__main__':
    main()                                                                    