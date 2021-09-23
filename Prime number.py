n=int(input("enter a number"))
a=0
for b in range(2,n):
    if n%b!=0:
        a+=1
if a==n-2:
    print(n,"is a prime number")
else:
    print(n,"is not a prime number")