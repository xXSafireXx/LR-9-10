from random import randint
n, m = 8, 8
x=0
z='no'
b=[-1,-1,-1,-1,-1,-1,-1,-1]
a = [[randint(-10, 10) for j in range(m)] for i in range(n)]
for i in range(8):
      b[i]=min(a[i])
      x+=b[i]
for i in range(8):
    if b[i]==x//8:
        z='yes'
print(a)
print()
print(b)
print(z)
