from collections import defaultdict
t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    matrix=[[0]*m for i in range(n)]
    for x in range(n):
        matrix[x]=list(map(int,input().split()))
        
    fwd_dig=defaultdict(int)
    bwd_dig=defaultdict(int)
    for i in range(n):
        for j in range(m):
            fwd_dig[i-j]+=matrix[i][j]
            bwd_dig[i+j]+=matrix[i][j]
            
    res=0
    for i in range(n):
        for j in range(m):
            summ=fwd_dig[i-j]+bwd_dig[i+j]-matrix[i][j]
            res=max(res,summ)
            
    print(res)
            
