v=int(input())
n=int(input())
from collections import defaultdict
adj_dic=defaultdict(list)
for i in range(v):
    adj_dic[i+1]=[]
for i in range(n):
    operations=list(map(int,input().split()))
    if operations[0]==1:
        adj_dic[operations[1]].append(operations[2])
        adj_dic[operations[2]].append(operations[1])
    elif adj_dic[operations[1]]!=[]:
        print(*adj_dic[operations[1]])
