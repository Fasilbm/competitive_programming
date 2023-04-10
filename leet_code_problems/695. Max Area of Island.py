class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        # Itrate over the grid until I find one
        # When i find 1 run dfs on that cell for the 4 diretions
        # when i finsish dfs on that particular island update max_area
        # continue until all cells are visited
        m=len(grid)
        n=len(grid[0])
        visited=set()
        max_island=0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        inbound= lambda row,col: 0<=row<m and 0<=col<n
        def dfs(grid,row,col,visited,max_island):
            nonlocal count
            visited.add((row,col))
            for r,c in directions:
                new_row=r+row
                new_col=c+col
                if inbound(new_row, new_col) and (new_row,new_col) not in visited:
                    if grid[new_row][new_col]==1:
                        count+=1
                        dfs(grid,new_row,new_col,visited,max_island)
                        
        for i in range(m):
            for j in range(n):
                if (i,j) not in visited and grid[i][j]==1:
                    count=1
                    dfs(grid,i,j,visited,max_island)
                    max_island=max(max_island,count)
                else:
                    visited.add((i,j))
        return max_island

