r,c=map(int,input().split())
mat=[]
for i in range(r):
  x=list(map(int,input().split()))
  mat.append(x)
k=[]
for i in range(r):
  s=0
  for j in range(c):
    s+=mat[i][j]
  k.append(s)
print(max(k))  