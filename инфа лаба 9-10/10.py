from random import randint
n, m = 8, 8
b=[1,1,1,1,1,1,1,1]
a = [[randint(-10, 10) for j in range(m)] for i in range(n)]
for i in range(8):
    x=0
    if a[i].count(max(a[i]))>1:
          b[i]=-1
print(a)
print()
print(b)
