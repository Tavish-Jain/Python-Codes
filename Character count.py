a=input("Enter a string value: ")
c=0
for i in range(65,91):
    b=chr(i)
    d=a.count(b)
    c+=d
print("Number of capital letters is:",c)
e=0
for i in range(97,122):
    b=chr(i)
    d=a.count(b)
    e+=d
print("Number of Small letters is:",e)
f=0
for i in range(0,10):
    b=str(i)
    d=a.count(b)
    f+=d
print("Number of numeric values is:",f)
print("Number of alphabets is:",c+e)
g=len(a)
print("Number of other characters is:",g-(c+e+f))