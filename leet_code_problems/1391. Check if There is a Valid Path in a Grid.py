class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:

        rep={}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                rep[i,j] = (i,j)
        roads = {
            1:[(0,-1),(0,1)],
            2:[(-1,0),(1,0)],
            3:[(0,-1),(1,0)],
            4:[(0,1),(1,0)],
            5:[(0,-1),(-1,0)],
            6:[(-1,0),(0,1)]
        }

        edges = []
        row = len(grid)
        col = len(grid[0])
        inbound = lambda r,c : 0 <= r < row and 0 <= c < col
        
        def find(node):
            while rep[node] != node:
                node = rep[node]
            return node
          
        def union(x,y):
            parent_x = find(x)
            parent_y = find(y)
            rep[parent_y] = rep[parent_x]
        
        def valid(x,y):
            for r,c in roads[grid[x][y]]:
                new_row = r + x
                new_col = c + y
                if inbound(new_row,new_col) and (-1*r,-1*c) in roads[grid[new_row][new_col]]:
                    edges.append([(x,y),(new_row,new_col)])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                valid(i,j)

        for i,j in edges:
            union(i,j)
                
        return find((0,0)) == find((row-1,col-1))
