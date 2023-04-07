v=int(input())
matrix=[]
for i in range(v):
    matrix.append(list(map(int,input().split())))
ans={}
for i in range(v):
    ans[i+1]=[]
for i in range(v):
    for j in range(v):
        if matrix[i][j]==1:
            ans[i+1].append(j+1)
for i,j in ans.items():
    print(len(ans[i]),*ans[i])
    



