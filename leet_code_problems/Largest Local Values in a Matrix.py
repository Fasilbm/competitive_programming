class Solution:
    def largestLocal(self, grid):
        n=len(grid[0])
        ans=[[0]*(n-2) for _ in range(n-2)]
        start_r,row=0,3
        start_c,col=0,3
        maxi=0
        while row<=n:
            maxi=0
            while col<=n:
                for i in range(start_r,row):
                    for j in range(start_c,col):

                        maxi=max(maxi,grid[i][j])
                ans[start_r][start_c]=maxi
                maxi=0
                start_c+=1
                col+=1
            start_c=0
            col=3
            start_r+=1
            row+=1
        return ans
