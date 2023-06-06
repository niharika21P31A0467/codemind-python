n=input()
u=""
for i in n:
  if i.isalpha():
     u=u+i
#print(u)
u=sorted(u)
j=0
for i in n:
  if i.isalpha():
     print(u[j],end="")
     j+=1
  else:
    print(i,end="")  