for k in range(0,6):
    N=65
    print(" "*k,end='')
    for j in range(k,6):
        print(chr(N),end='')
        N+=1
    print()
print("pattern 2:\n")
for i in range(6,0,-1):
    print(" "*i,end="")
    for j in range(i,7):
        print("*",end="")
    print()
print()
n=int(input("enter a value for no. of lines: "))
for i in range(0,n):
    N=97
    print(" "*i,end='')
    for j in range(n,i,-1):
        print(chr(N),end='')
        N+=1
    print()
for a in range (2):
    print(a)