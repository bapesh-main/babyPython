def cipher():
    m=int(raw_input("Enter m value:"))
    n=int(raw_input("Enter n value:"))
    if n<=m:
        print("Unexpected input. Exiting function")
        return;
    for i in xrange(m,(n+1)):
        charcipher(i)
    
def charcipher(num):
    x=num%26
    y=int(num/26)
    if y>26:
        print("Number is greater than 676. Exiting function")
        return;
    if x==0:
        b='Z'
        a=''
        if y>1:
            a=chr(64+y-1)
        print(a+b)
    else:
        if y>0:
            a=chr(64+y)
            b=chr(64+x)
            print(a+b)
        else:
            a=chr(64+x)
            print(a)

cipher()