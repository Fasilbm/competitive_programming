n,k=input().split()
arr=list(map(int,input().split()))
arr.sort()
from collections import Counter
count=Counter(arr)
sum_=0
ans=sorted(count.keys())
for i in ans:
    sum_+=count[i]
    if sum_==int(k):
        print(i)
        break
    if int(k)!=0 and sum_>int(k):
        print(-1)
        break

if int(k)==0 and arr[0]>1:
    print(arr[0]-1)
elif int(k)==0 and arr[0]<=1:
    print(-1)


