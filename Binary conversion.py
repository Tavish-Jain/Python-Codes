def d_to_b():
    a=float(input("Enter a Number here: "))
    i=int(a)
    s=""
    while i>0:
        s+=str(i%2)
        i=i//2
    fs=""
    for j in range(-1,-len(s)-1,-1):
        fs+=s[j]
    b=len(str(a))
    c=len(str(int(a)))
    d=b-c
    f=a-int(a)
    f=round(f,d)
    fs+="."
    g=f
    p=f
    x=0
    while g>0:
        fs+=str(int(g*2))
        n=int(g*2)
        g*=2
        b=len(str(g))
        c=len(str(n))
        d=b-c
        g-=n
        g=round(g,d)
        x+=1
        h=f
        for z in range (0,x):
            if h==g:
                g=0
            else:
                h*=2
                q=int(h)
                b=len(str(q))
                c=len(str(h))
                d=c-b
                h-=q
                h=round(h,d)
    print(a,"in Binary Format is",fs)
def b_to_d:
    a=float(input("Enter a binary number: "))
    b=int(a)
    b=str(b)
    dn=0
    e=0
    for i in range(-1,-len(b)-1,-1):
        dn+=int(b[i])*2**e
        e+=1
    f=a-int(b)
    l1=len(str(a))
    l2=len(b)
    l=l1-l2
    f=round(f,l)
    f=str(f)
    e=-1
    for i in range(2,len(f)):
        dn+=int(f[i])*2**e
        e-=1
    print(a,"in decimal number system is",dn)
def o_to_b():
    a=float(input("Enter an octal number: "))
    c=""
    if int(a)==a:
        b=str(int(a))
        for i in range(0,len(b)):
            if b[i]=='0':
                c+="000"
            elif b[i]=="1":
                c+="001"
            elif b[i]=="2":
                c+="010"
            elif b[i]=="3":
                c+="011"
            elif b[i]=="4":
                c+="100"
            elif b[i]=="5":
                c+="101"
            elif b[i]=="6":
                c+="110"
            elif b[i]=="7":
                c+="111"
            else:
                print("Oops! Guess you gave an invalid input.")
                break
        else:
            print(a,"in binary format is",c)
    else:
        b=str(a)
        for i in range(0,len(b)):
            if b[i]=='0':
                c+="000"
            elif b[i]=="1":
                c+="001"
            elif b[i]=="2":
                c+="010"
            elif b[i]=="3":
                c+="011"
            elif b[i]=="4":
                c+="100"
            elif b[i]=="5":
                c+="101"
            elif b[i]=="6":
                c+="110"
            elif b[i]=="7":
                c+="111"
            elif b[i]==".":
                c+="."
            else:
                print("Oops! Guess you gave an invalid input.")
                break
        else:
            print(a,"in binary format is",c)
def b_to_o():
    a=float(input("Enter a Binary Number: "))
    b=int(a)
    b=str(b)
    n=0
    on=""
    l=len(b)//3
    if len(b)==3*l:
        c=b
    else:
        l1=3*(l+1)-len(b)
        c=""
        for i in range(0,l1):
            c+="0"
        c+=b
    for i in range(-1,-len(c),-3):
        e=2
        n=0
        for j in range(i-2,i+1):
            n+=int(c[j])*(2**e)
            e-=1
        on+=str(n)
    print(a,"in octal number system is",on)
def d_to_o():
    a=float(input("Enter a number: "))
    i=int(a)
    s=""
    while i>0:
        s+=str(i%8)
        i=i//8
    fs=""
    for j in range(-1,-len(s)-1,-1):
        fs+=s[j]
    b=len(str(a))
    c=len(str(int(a)))
    d=b-c
    f=a-int(a)
    f=round(f,d)
    fs+="."
    g=f
    p=f
    x=0
    while g>0:
        fs+=str(int(g*8))
        n=int(g*8)
        g*=8
        b=len(str(g))
        c=len(str(n))
        d=b-c
        g-=n
        g=round(g,d)
        x+=1
        h=f
        for z in range (0,x):
            if h==g:
                g=0
            else:
                h*=8
                q=int(h)
                b=len(str(q))
                c=len(str(h))
                d=c-b
                h-=q
                h=round(h,d)
    print(a,"in Octal Number System is",fs)
def o_to_d():
    a=float(input("Enter an octal number: "))
    b=int(a)
    b=str(b)
    dn=0
    e=0
    for i in range(-1,-len(b)-1,-1):
        dn+=int(b[i])*8**e
        e+=1
    f=a-int(b)
    l1=len(str(a))
    l2=len(b)
    l=l1-l2
    f=round(f,l)
    f=str(f)
    e=-1
    for i in range(2,len(f)):
        dn+=int(f[i])*8**e
        e-=1
    print(a,"in decimal number system is",dn)
def h_to_b():
    a=input("Enter a hexadecimal number: ")
    c=""
    b=a.upper()
    for i in range(0,len(b)):
        if b[i]=='0':
            c+="0000"
        elif b[i]=="1":
            c+="0001"
        elif b[i]=="2":
            c+="0010"
        elif b[i]=="3":
            c+="0011"
        elif b[i]=="4":
            c+="0100"
        elif b[i]=="5":
            c+="0101"
        elif b[i]=="6":
            c+="0110"
        elif b[i]=="7":
            c+="0111"
        elif b[i]=="8":
            c+="1000"
        elif b[i]=="9":
            c+="1001"
        elif b[i]=="A":
            c+="1010"
        elif b[i]=="B":
            c+="1011"
        elif b[i]=="C":
            c+="1100"
        elif b[i]=="D":
            c+="1101"
        elif b[i]=="E":
            c+="1110"
        elif b[i]=="F":
            c+="1111"
        elif b[i]==".":
            c+="."
        else:
            print("Oops! Guess you gave an invalid input.")
            break
    else:
        print(b,"in binary format is",c)
def b_to_h():
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
    else:
        print(a,"in hexadecimal number system is",fn)