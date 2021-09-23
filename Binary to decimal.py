a=float(input("Enter a Binary Number: "))
b=int(a)
b=str(b)
n=0
on=""
l=len(b)//4
if len(b)==4*l:
    c=b
else:
    l1=4*(l+1)-len(b)
    c=""
    for i in range(0,l1):
        c+="0"
    c+=b
hn=""
for i in range(-1,-len(c),-4):
    e=3
    n=0
    for j in range(i-3,i+1):
        n+=int(c[j])*(2**e)
        e-=1
    if n>9:
        A=n-10
        N=65
        hn+=chr(N+A)
    else:
        hn+=str(n)
fn=""
for i in range(-1,-len(hn)-1,-1):
    fn+=hn[i]
b=a-int(b)
l1=len(str(a))
l2=len(str(int(a)))
l=l1-l2
b=round(b,l)
b=str(b)
fn+="."
l1=(len(b)-2)//4
if len(b)-2==l1*4:
    b=b
else:
    l2=4*(l1+1)-(len(b)-2)
    for i in range(0,l2):
        b+="0"
for i in range(2,len(b),4):
    e=0
    n=0
    for j in range(i+3,i-1,-1):
        n+=int(b[j])*2**e
        e+=1
    if n>9:
        A=n-10
        N=65
        fn+=chr(N+A)
    else:
        fn+=str(n)
else:
    print(a,"in hexadecimal number system is",fn)