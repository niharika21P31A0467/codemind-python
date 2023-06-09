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
p=max(k)
h=[]
for i in range(r):
  s=0
  for j in range(c):
    s+=mat[i][j]
  h.append(s)
q=max(h)
o=[]
o.append(p)
o.append(q)
print(max(o))
    
    