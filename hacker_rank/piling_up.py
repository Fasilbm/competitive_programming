N=int(input())
for i in range(N):
    B=int(input())
    blocks= list(map(int,input().strip().split(' ')))
    l=0
    r=B-1
    stack=[]
    while l<=r:
        if not stack:
            if blocks[l]<blocks[r]:
                stack.append(blocks[r])
                r-=1
            else:
                stack.append(blocks[l])
                l+=1
        elif blocks[l]<=blocks[r] and blocks[r]<=stack[-1]:
            stack.append(blocks[r])
            r-=1
        elif  blocks[l]>blocks[r] and blocks[l]<=stack[-1]:
            stack.append(blocks[l])
            l+=1
        else:
            break
    if len(stack)!=B:
        print("No")
    else:
        print("Yes")
            
            
        
            
            
    
    
