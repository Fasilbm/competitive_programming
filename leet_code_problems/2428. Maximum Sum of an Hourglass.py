class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        pot=[]
        row=len(grid)
        col=len(grid[0])
        for i in range(row-2):
            for j in range(col-2):
                pot.append(grid[i][j]+grid[i][j+1]+grid[i][j+2]+grid[i+1][j+1]+grid[i+2][j]+grid[i+2][j+1]+grid[i+2][j+2])
        return(max(pot))
