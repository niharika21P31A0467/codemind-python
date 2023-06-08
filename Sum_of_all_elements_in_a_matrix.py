r,c=map(int,input().split())
mat=[]
for i in range(r):
  x=list(map(int,input().split()))
  mat.append(x)
p=[]
for i in mat:
  p.append(sum(i))
print(sum(p))  

  
  