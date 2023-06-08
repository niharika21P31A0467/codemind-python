r,c=map(int,input().split())
mat=[list(map(int,input().split()))for i in range(r)]
k=[]
p=[]
m=[]
for i in range(1,len(mat)-1,1):
  k.append(mat[i])
for i in k:  
  for j in range(1,len(i)-1,1):
    p.append(i[j])
print(sum(p))    