n,m = (input().split())
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
p1=0
p2=0
count=0
ans=[]
while p2<len(arr2):
    if p1 <len(arr1) and arr2[p2]>arr1[p1]:
        count+=1
        p1+=1
    else:
        ans.append(count)
        p2+=1
print(*ans)
