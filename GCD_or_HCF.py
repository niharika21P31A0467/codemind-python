a,b=map(int,input().split())
i=1
while(i<=a and i<=b):
 if a%i==0 and b%i==0:
    gcd=i
 i+=1
print(gcd) 
     