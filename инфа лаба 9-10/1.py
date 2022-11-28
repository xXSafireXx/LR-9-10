a=list(map(int,input().split()))
b=1
def prois(b,c):
    b=b*c
    return(b)
for i in range(1,len(a),2):
   c=a[i]
   b=prois(b,c)
print(b)
