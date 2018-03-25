import math
def startup():
    num=int(raw_input("Enter the number:"))
    if num>100000:
        print("Number is outside accepted range. Exiting function")
        return
    root=int(math.sqrt(num))
    factorisation(num,root)
    isprime(num,root)

def factorisation(num,root):
    print("Factors of "+str(num)+" are:")
    factors=[]
    for i in xrange(1,(root+1)):
        if num%i==0:
            if i==1:
                factors.append(num/i)
                #print(str(num/i))
            else:
                factors.append(i)
                factors.append(num/i)
                #print(str(i)+','+str(num/i))
    factors.sort()
    print str(factors)[1:-1]

def isprime(num,root):
    flag=0
    for i in xrange(2,(root+1)):
        if num%i==0:
            flag=1
            break
    if flag==1:
        print(str(num)+" is NOT PRIME")
    else:
        print(str(num)+" is PRIME")

startup()