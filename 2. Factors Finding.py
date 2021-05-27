n=int(input())
c=1
s=[]
for i in range(1,(n//2)+1):
    if(n%i==0):
        c+=1
        s.append(i)
s.append(n)
print(c)
print(*s)
