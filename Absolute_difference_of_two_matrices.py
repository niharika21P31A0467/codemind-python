r=int(input())
a=[list(map(int,input().split()))for i in range(r)]
b=[list(map(int,input().split()))for j in range(r)]
for i in range(r):
  s=[]
  for j in range(r):
    s.append(abs(a[i][j]-b[i][j]))
  print(*s)    