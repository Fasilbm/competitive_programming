from collections import Counter
t=int(input())
for i in range(t):
    n=list(map(int,input().split(" ")))
  
        
    planets=list(map(int,input().split(" ")))
        
    count=Counter(planets)
    ans=0
    
    for i in count.values():
        
        if i>1 and i>n[1]:
            ans+=n[1]
        elif i>1 and i<=n[1]:
            ans+=i
        else:
            ans+=1
    print(ans)
