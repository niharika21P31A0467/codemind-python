r,c=map(int,input().split())
mat=[]
for i in range(r):
  x=list(map(int,input().split()))
  mat.append(x)
for i in range(c):
  s=0
  p=[]
  for j in range(r):
    s+=mat[j][i]  
  p.append(s)
  for i in p:
    print(i,end=' ')  