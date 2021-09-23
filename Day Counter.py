print("Enter the following Details (enter valid dates please): ")
d1=int(input("Enter your first date(only date): "))
m1=int(input("Enter your first month(month number): "))
y1=int(input("Enter your first year(as YYYY cofiguration): "))
d2=int(input("Enter last date(only date): "))
m2=int(input("Enter last month(month number): "))
y2=int(input("Enter last year(in YYYY configuration: "))
a=0
b=m1
if m1<8:
    if m1%2==0:
        if m1==2:
            if y1%4==0:
                for i in range(d1,30):
                    a+=1
            else:
                for i in range(d1,29):
                    a+=1
        else:
            for i in range(d1,31):
                a+=1
    else:
            for i in range(d1,32):
                a+=1
else:
    if m1%2==0:
        for j in range(d1,32):
            a+=1
    else:
        for j in range(d1,31):
            a+=1
b+=1
if b>12:
    b=1
    y1+=1
for l in range (b,13):
    if l<8:
        if l%2==0:
            if l==2:
                if y1%4==0:
                    a+=29
                else:
                    a+=28
            else:
                a+=30
        else:
            a+=31
    else:
        if l%2==0:
            a+=31
        else:
            a+=30
for k in range(y1+1,y2):
    if k%4==0:
        a+=366
    else:
        a+=365
for m in range (1,m2):
    if m<8:
        if m%2==0:
            if m==2:
                if y1%4==0:
                    a+=29
                else:
                    a+=28
            else:
                a+=30
        else:
            a+=31
    else:
        if m%2==0:
            a+=31
        else:
            a+=30
for n in range(0,d2):
    a+=1
print("you are",a,"days")