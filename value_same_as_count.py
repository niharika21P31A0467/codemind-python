n=int(input())
a=list(map(int,input().split()))
c=0
for i in sorted(set(a),key=a.index):
    if a.count(i)==i:
        c+=1
print(c)
