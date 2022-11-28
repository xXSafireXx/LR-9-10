from random import randint
n, m = 8, 8
b=[-1,-1,-1,-1,-1,-1,-1,-1]
a = [[randint(-1, 10) for j in range(m)] for i in range(n)]
for i in range(8):
    for j in range(7):
     if a[i][j]+a[i][j+1]==7:
      b[i]=1
      break
print(a)
print()
print(b)
