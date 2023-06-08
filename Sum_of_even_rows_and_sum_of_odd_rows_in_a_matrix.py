r,c=map(int,input().split())
mat=[]
for i in range(r):
  x=list(map(int,input().split()))
  mat.append(x)
a=[]
b=[]
for i in range(0,len(mat),2):
  a.append(mat[i])
for i in range(1,len(mat),2):
  b.append(mat[i]) 
l=[]
k=[]
for i in a:
  l.append(sum(i)) 
for i in b:
  k.append(sum(i))
p=sum(k)
t=sum(l)
print(t,p)
    