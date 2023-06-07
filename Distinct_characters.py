a=input()
a=a.lower()
brr=[]
for i in a:
  if a.count(i)==1 and i not in' ':
     brr.append(i)
crr=sorted(brr)
for i in crr:
  print(i,end="")