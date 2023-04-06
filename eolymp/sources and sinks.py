n=int(input())
matrix=[]
for i in range(n):
    matrix.append(list(map(int,input().split())))
sources=set()
sinks=set()
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j]==1:
            sources.add(i+1)
            sinks.add(j+1)
sources1=[]
sinks1=[]
for i in sources:
    if i not in sinks:
        sources1.append(i)
for i in sinks:
    if i not in sources:
        sinks1.append(i)
for i in range(1,n+1):
    if i not in sources and i not in sinks: 
            sources1.append(i)
            sinks1.append(i)
sources1.sort()
sinks1.sort()
print(len(sources1),*sources1)
print(len(sinks1),*sinks1)
