a=list(map(int,input().split()))
b=list(map(int,input().split()))
print(a)
print(b)
x=0
y=0
i=0
for i in range(len(a)):
    if a[i]>0:
        x+=a[i]
i=0
for i in range(len(b)):
    if b[i]>0:
        y+=b[i]
if x>y:
    for i in range(len(b)):
                           b[i]=b[i]*10
    print(b)
if x<y:
                   for i in range(len(a)):
                           a[i]=a[i]*10
                   print(a)
