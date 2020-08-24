n = int(input())
prime=0
for i in range(n-1,0,-1):
    if i==2:
        prime = i
    elif(i>2):
        st=True
        for j in range(2,int(n**0.5)+1):
            if(i%j==0):
                st=False
                break
        if(st):
            prime = i
            break
s_prime=0      
for i in range(n+1,n+(n-prime)):
    if(i>2):
        st=True
        for j in range(2,int(n**0.5)+1):
            if(i%j==0):
                st=False
                break
        if(st):
            s_prime=i
            break
    else:
        break
        
if(s_prime!=0 and (n-prime > s_prime-n)):
    print(s_prime)
else:
    print(prime)
    
    
    
 # input = 10
 # output = 11
