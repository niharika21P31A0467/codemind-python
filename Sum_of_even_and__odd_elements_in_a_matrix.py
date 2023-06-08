r,c=map(int,input().split())
mat=[]
for i in range(r):
  x=list(map(int,input().split()))
  mat.append(x)
k=[]
for i in mat:
  for j in i:
    k.append(j)
m=[]
s=[]
for i in k:
  if i%2==0:
     m.append(i)
  else:
    s.append(i)
print(sum(m),sum(s))
