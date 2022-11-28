import random
a=[random.randint(0, 100000) for i in range(10)]
i=0
n=11
m=11
b=[random.randint(0, 100000) for i in range(10)]
print(a)
print(b)
for i in range(len(a)):
    if a[i]%5==0:n=i
    if b[i]%5==0:m=i
if n>m:
    b[b.index(max(b))]=0
    for i in range(a.index(min(a)),len(a),1):
        a[i]*=2
    print(a)
    print(b)
else:
    a[a.index(max(a))]=0
    print(a)
    for i in range(b.index(min(b)),len(b),1):
        b[i]*=2
    print(b)
