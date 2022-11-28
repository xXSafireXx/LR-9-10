from random import randint
n, m = 6, 8
b=[]
a = [[randint(1, 10) for j in range(m)] for i in range(n)]
for i in range(6):
    for j in range(8):
     if abs(a[i][j])>4:
      b.append(a[i][j])
      break
    else:
     b.append(0)
print(a)
print()
print(b)
