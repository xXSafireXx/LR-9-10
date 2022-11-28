a=list(map(int,input().split()))
x=0
def num(a,i,x):
    if a[i]<x:x=i
    return x
for i in range(len(a)-1,0,-1):
               x=num(a,i,x)
               if x!=0:
                   break
print(x)
               
