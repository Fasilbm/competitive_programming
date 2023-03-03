class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:

        possible=float("inf")
        maxi_of_b=float("-inf")

        for i  in range(len(grid)):

            for j in range(1,len(grid[0])):

                grid[i][j] += grid[i][j-1]


        for j in range(len(grid[0])):

                if j==0:

                    left=0
                    right=grid[0][-1]-grid[0][0]

                    maxi_of_b=max(left,right)
                    possible=min(possible,maxi_of_b)

                elif j==len(grid[0])-1:

                    left=grid[1][j-1]
                    right=0
                    
                    maxi_of_b=max(left,right)
                    possible=min(possible,maxi_of_b)

                else:

                    left=grid[1][j-1]
                    right=grid[0][-1]-grid[0][j]

                    maxi_of_b=max(left,right)
                    possible=min(possible,maxi_of_b)

                

        return possible



