n=5
for i in range(1,n+1):
    print(" "*(n-i),"* "*i)
print()
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=' ')
    print()
print()
for i in range(1,n+1):
    for j in range(i,n+1):
        print(i,end=' ')
    print()
print()
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()
print()
for i in range(n,0,-1):
    for j in range (1,i+1):
        print(i,end=' ')
    print()
print()
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(n,end=' ')
    print()
print()
for i in range(1,n+1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()
print()
for i in range(n,-1,-1):
    for j in range(0,i+1):
        print(j,end=' ')
    print()
print()
a=1
for a in range(a,n+1):
    for j in range(1,i+1):
        print(a,end=' ')
        a+=1
    print()