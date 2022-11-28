a=list(map(int,input().split()))
b=list(map(int,input().split()))
print(a)
print(b)
def o(k):
    l=0
    for i in range(len(k)):
     if k[i]>0:
        l+=k[i]
        return(l)
def p(k):
    for i in range(len(k)):
                           k[i]=k[i]*10
    print(k)
    
x=0
y=0
i=0
x=o(a)
i=0
y=o(b)
if x>y:
    p(b)
else:
    p(a)

