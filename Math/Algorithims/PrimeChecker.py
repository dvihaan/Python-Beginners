from math import sqrt
def PrimeChecker(x):
    x2 = int(x)
    p = True
    for i in range(2,round(sqrt(x2))+1,1):
        if x2%i == 0:
            p = False
            break
    return p

def main():
    number = input("Insert a number: ")
    isprime = PrimeChecker(number)
    
    if isprime == True: print("your number is a prime number!")
    if isprime == False: print("your number isn't a prime number")

if __name__ == '__main__':
    main()