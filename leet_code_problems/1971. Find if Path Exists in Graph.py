def validPath(n: int, edges, source: int, destination: int):
    connected={i:i for i in range(n)}

    def union(x,y):
        while connected[x] != x:
            x = connected[x]

        while connected[y]!=y:
            y = connected[y]

        connected[y]=connected[x]

    def find(x,y):
        while connected[x] != x:
            x = connected[x]

        while connected[y]!=y:
            y = connected[y]

        return connected[x]==connected[y]

    for i,j in edges:
        union(i,j)

    return find(source,destination)
