n=int(input())
from collections import deque
for i in range(n):
    
    length=int(input())
    my_list=list(map(int,input().split(" ")))
    my_list.sort()
    de=deque(my_list)
    l=0
    r=1
    while len(de)>1:
        if de[r]-de[l]<=1:
            de.popleft()
        else:
            print("NO")
            break
    if len(de)==1:
        print("YES")
        

        
    
