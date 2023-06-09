r,c=map(int,input().split())
mat=[]
for i in range(r):
  x=list(map(int,input().split()))
  mat.append(x)
for i in range(r):
  s=0
  p=[]
  for j in range(c):
    s+=mat[i][j]
  p.append(s)
  for i in p:
    print(i,end=' ')  
    