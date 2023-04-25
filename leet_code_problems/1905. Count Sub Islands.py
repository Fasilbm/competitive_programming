class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:

        directions=[(-1,0),(1,0),(0,1),(0,-1)]
        m=len(grid1)
        n=len(grid1[0])
        inbound=lambda row,col: 0<=row<m and 0<=col<n
        visited=set()
        imposter=set()
        def dfs1(grid2,grid1,row,col,visited,imposter):
            visited.add((row,col))
            for i,j in directions:
                new_row=row+i
                new_col=col+j
                if inbound(new_row,new_col) and (new_row,new_col) not in visited:
                    if grid2[new_row][new_col]==1:
                        imposter.add((new_row,new_col))
                        dfs1(grid2,grid1,new_row,new_col,visited,imposter)
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 and grid1[i][j]==0 and (i,j) not in visited:
                    imposter.add((i,j))
                    dfs1(grid2,grid1,i,j,visited,imposter)
        

        for i in range(m):
            for j in range(n):
                if grid2[i][j]==1 and (i,j) not in imposter:
                    grid2[i][j]=1
                elif  grid2[i][j]==1 and (i,j) in imposter:
                     grid2[i][j]=0
        new_visited=set()
        def dfs2(row,col,new_visted):
            new_visited.add((row,col))
            for i,j in directions:
                new_row=row+i
                new_col=col+j
                if inbound(new_row,new_col) and (new_row,new_col) not in new_visited:
                    if grid2[new_row][new_col]==1:
                        dfs2(new_row,new_col,new_visited)
        count=0
        for i in range(m):
            for j in range(n):
                if grid2[i][j]==1 and (i,j) not in new_visited:
                    dfs2(i,j,new_visited)
                    count+=1

        return count

                 
        

        





