l=input().lower().split()
c_c=list(l[0])
x=[]
for i in range(1,len(l)):
  for j in c_c:
    if j in l[i] and j not in x:
       x.append(j)
  c_c=x
  x=[]
if len(c_c)==0:
   print(-1)
else:
  print(min(c_c))    
  