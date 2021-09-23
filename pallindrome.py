n=int(input("enter a number: "))
a=n
sum=0
while a>0:
    d=a%10
    sum+=d
    a=int(a/10)
print ("sum of digits of",n,"= ", sum)