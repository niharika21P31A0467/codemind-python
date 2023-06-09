r,c=map(int,input().split())
mat=[]
for i in range(r):
  x=list(map(int,input().split()))
  mat.append(x)
k=[]
for i in range(c):
  s=0
  for j in range(r):
    s+=mat[j][i]
  k.append(s)
print(max(k))  
  