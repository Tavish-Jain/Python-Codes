A="     ##     \n    ####    \n   ##  ##   \n  ########  \n ##      ## \n            "
B=" ########   \n ##     ##  \n ##     ##  \n ########   \n ##     ##  \n ##      ## \n ##      ## \n #########  \n            "
C="    ####    \n  ###  ##   \n ##         \n ##         \n ##     ##  \n  ###  ##   \n    ####    \n            "
D=" #######    \n ##    ##   \n ##     ##  \n ##      ## \n ##      ## \n ##     ##  \n ########   \n            "
E=" #########  \n ##         \n ##         \n ######     \n ##         \n ##         \n #########  \n            "
F=" #########  \n ##         \n ##         \n ######     \n ##         \n ##         \n ##         \n            "
G="    #####   \n  ###   ### \n ##      ## \n ##         \n ##   ##### \n ###     ## \n   #######  \n            "
H=" ##      ## \n ##      ## \n ##      ## \n ########## \n ##      ## \n ##      ## \n ##      ## \n            "
I=" ########## \n     ##     \n     ##     \n     ##     \n     ##     \n     ##     \n ########## \n            "
J=" ########## \n     ##     \n     ##     \n     ##     \n     ##     \n ##  ##     \n  ####      \n            "
K="  ##     ## \n  ##    ##  \n  ##   ##   \n  ######    \n  ##   ##   \n  ##    ##  \n  ##    ##  \n            "
L="  ##        \n  ##        \n  ##        \n  ##        \n  ##        \n  ##        \n  ######### \n            "
M=" ##      ## \n ###    ### \n ## #### ## \n ##  ##  ## \n ##      ## \n ##      ## \n ##      ## \n            "
N=" ###     ## \n ####    ## \n ## ##   ## \n ##  ##  ## \n ##   ## ## \n ##    #### \n ##     ### \n            "
O="    ####    \n   ##  ##   \n  ##    ##  \n  ##    ##  \n  ##    ##  \n   ##  ##   \n    ####    \n            "
P=" ########   \n ##     ##  \n ##     ##  \n ########   \n ##         \n ##         \n ##         \n            "
Q="    ####    \n   ##  ##   \n  ##    ##  \n  ##   ##   \n   #####    \n  ##  ###   \n        ##  \n            "
R=" #######    \n ##    ##   \n ##    ##   \n #######    \n ##    ##   \n ##     ##  \n ##     ##  \n            "
S="   ######   \n ###    ### \n###         \n ###        \n  #######   \n        ### \n ##       ##\n  ###   ### \n    #####   \n            "
T=" ########## \n     ##     \n     ##     \n     ##     \n     ##     \n     ##     \n            "
U="  ##    ##  \n  ##    ##  \n  ##    ##  \n  ##    ##  \n   ##  ##   \n    ####    \n            "
V=" ##      ## \n  ##    ##  \n   ##  ##   \n    ####    \n     ##     \n            "
W=" ##      ## \n ##      ## \n ##      ## \n ##  ##  ## \n ## #### ## \n ####  #### \n ##      ## \n            "
X=" ##      ## \n  ##    ##  \n   ##  ##   \n    ####    \n   ##  ##   \n  ##    ##  \n ##      ## \n            "
Y=" ##      ## \n  ##    ##  \n   ##  ##   \n    ####    \n     ##     \n     ##     \n     ##     \n            "
Z="  ########  \n       ##   \n      ##    \n     ##     \n    ##      \n   ##       \n  ########  \n            "
a=input("Enter Your Name: ")
b=a.upper()
c=a.replace(" ","")
if c.isalpha():
    print("            ")
    for i in range(0,len(b)):
        if b[i]=="A":
            print(A)
        elif b[i]=="B":
            print(B)
        elif b[i]=="C":
            print(C)
        elif b[i]=="D":
            print(D)
        elif b[i]=="F":
            print(F)
        elif b[i]=="G":
            print(G)
        elif b[i]=="H":
            print(H)
        elif b[i]=="I":
            print(I)
        elif b[i]=="J":
            print(J)
        elif b[i]=="K":
            print(K)
        elif b[i]=="L":
            print(L)
        elif b[i]=="M":
            print(M)
        elif b[i]=="N":
            print(N)
        elif b[i]=="O":
            print(O)
        elif b[i]=="P":
            print(P)
        elif b[i]=="Q":
            print(Q)
        elif b[i]=="R":
            print(R)
        elif b[i]=="S":
            print(S)
        elif b[i]=="T":
            print(T)
        elif b[i]=="U":
            print(U)
        elif b[i]=="V":
            print(V)
        elif b[i]=="W":
            print(W)
        elif b[i]=="X":
            print(X)
        elif b[i]=="Y":
            print(Y)
        elif b[i]=="Z":
            print(Z)
        elif b[i]=="E":
            print(E)
        elif b[i]==" ":
            print("            \n            \n            \n            ")
else:
    print("Oops! Invalid Values Entered!")