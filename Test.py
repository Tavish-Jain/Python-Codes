print("first pattern")
for a in range(1,7):
    for b in range(1,a):
        print(b,end="")
    print()
print("\n")
print("second pattern")
i=int(input("enter a number"))
a=0
for b in range(0,i+1):
    a+=b
else:
    print(a)
print("\n")
print("third pattern")
n=int(input("enter a number whos table should be displayed: "))
for a in range(1,11):
    print(n,"x",a,"= ",n*a)
else:
    print("\n")
print("fourth pattern")
c=int(input("enter a number"))
for a in range(1,101):
    if a%c==0:
        print(a,end=", ")
else:
    print("these are the multiples of ",c," in untill 100")
print()
print("fifth pattern")
for a in range(5,0,-1):
    for i in range(a,0,-1):
        print(i,end="")
    print()
else:
    print()
print("sixth pattern")
l1=[10,20,30,40,50]
for a in l1:
    print(60-a)
else:
    print()
print("next pattern")
for a in range(-10,0):
    print(a)
else:
    print("Done!")
    print()
print("next pattern")
for a in range(25,51):
    for i in range (2,51):
        if a%i!=0:
            print(a)