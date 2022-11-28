a=list(map(int,input().split()))
x=[]
b=1000000000000000000000
c=-100000000000000000000
for i in range(len(a)):
    x.append(a[i])
def min(b,n):
    if b>n: b=n
    return b
def maxotr(c,m):
    if (m<0) and (c<m): c=m
    return(c)
for i in range(len(a)):
    n=abs(a[i])
    m=a[i]
    b=min(b,n)
    c=maxotr(c,m)
print(b,' ',c)
