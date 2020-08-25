n=int(input())
lines=[]
for i in range(n):
    lines.append(input())

def iscolor(color):
    if(3<=len(color)<=6):
        try:
            temp = int(color,16)
            return color
        except:
            pass

brace=0

for i in lines:
    
    if(i.find("{")!=-1):
        brace=1
        
    elif(brace and len(i)>1):
        
        k=0
        hash_count = i.count("#")
        
        if(hash_count):
            
            for j in range (hash_count):
                hash_index = i.find("#",k,len(i))
                color=""
                for k in range(hash_index+1,len(i)):
                    if(i[k].isalnum()):
                        color+=i[k]
                    else:
                        break
                res = iscolor(color)
                if(res):
                    print("#"+res)
    elif(i.find("}")!=-1):
        brace=0
