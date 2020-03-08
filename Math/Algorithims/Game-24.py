def getsol(a,b,trgt,ops):
    if a+b == trgt:
        print(ops.replace("()","({}+{})".format(a,b)))
    if a-b == trgt:
        print(ops.replace("()","({}-{})".format(a,b)))
    if b-a == trgt:
        print(ops.replace("()","({}-{})".format(b,a)))
    if a*b == trgt:
        print(ops.replace("()","({}*{})".format(a,b)))
    if a/b == trgt:
        print(ops.replace("()","({}÷{})".format(a,b)))
    if b/a == trgt:
        print(ops.replace("()","({}÷{})".format(b,a)))
    

def checktarget(numbers,trgt,ops):
    print("Numbers = "+str(numbers)+", Target = "+str(trgt)+", Ops = "+ops)
    if len(numbers) == 2:
        getsol(numbers[0],numbers[1],trgt,ops)
    else:
        for i in range(len(numbers)):
            n = numbers[i]
            restnumbers = numbers[:i]+numbers[i+1:]
            checktarget(restnumbers,trgt-n,ops.replace("()", "({}+())".format(n)))
            checktarget(restnumbers,-trgt-n,ops.replace("()", "({}-())".format(n)))
            checktarget(restnumbers,trgt+n,ops.replace("()", "(()-{})".format(n)))
            if n != 0:
                checktarget(restnumbers,int(trgt/n),ops.replace("()", "(()*{})".format(n)))
            if trgt != 0:
                checktarget(restnumbers,int(n/trgt),ops.replace("()", "(()÷{})".format(n)))
            checktarget(restnumbers,trgt*n,ops.replace("()", "({}÷()))".format(n)))

def main():
    nums = [8,1,8,3]
    checktarget(nums, 24, "()")

if __name__== "__main__":
  main()
