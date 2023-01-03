# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

n=int(input())
rooms=list(map(int,input().split()))
count=Counter(rooms)
for i in count.keys():
    if count[i]== 1:
        print(i)
