l=0
r=0
n=list(map(int,input().split(" ")))
list_1=list(map(int,input().split(" ")))
list_2=list(map(int,input().split(" ")))
merged=[]

while l<n[0] and r<n[1]:
    
    if list_1[l]<=list_2[r]:
        merged.append(list_1[l])
        l+=1
    else:
        merged.append(list_2[r])
        r+=1
        
while l<n[0]:
    merged.append(list_1[l])
    l+=1
while r<n[1]:
    merged.append(list_2[r])
    r+=1
    
print(*merged)
    
