a=input("Enter a string: ")
p=""
for i in range(0,len(a)):
    b=ord(a[i])
    c=b
    s=""
    while c>0:
        s+=str(c%2)
        c=int(c/2)
    n=8-len(s)
    for i in range(0,n):
        s+="0"
    for i in range(-1,-len(s)-1,-1):
        p+=s[i]
    p+=" "
print(p)

n=8-len(s)
for i in range(0,n):
    s+="0"